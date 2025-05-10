from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from pyperclip import copy

from petstagram.common.forms import AddCommentForm, SearchForm
from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo


# Create your views here.
def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = AddCommentForm()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        all_photos = all_photos.filter(
            tagged_pets__name__icontains=search_form.cleaned_data['search_text']
        )

    page = request.GET.get('page')
    photos_per_page = 1
    paginator = Paginator(all_photos, photos_per_page)

    try:
        all_photos = paginator.page(page)
    except PageNotAnInteger:
        all_photos = paginator.page(1)
    except EmptyPage:
        all_photos = paginator.page(paginator.num_pages)

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context=context)


def like_unlike_photo(request, photo_id: int):
    like = Like.objects.filter(
        to_photo_id=photo_id
    ).first()

    if like:
        like.delete()
    else:
        like = Like(
            to_photo_id=photo_id
        )
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


def copy_link_to_clipboard(request, pk: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', pk))

    return redirect(request.META.get('HTTP_REFERER') + f"#{pk}")


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = get_object_or_404(Photo, id=photo_id)
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

    return redirect(request.META.get('HTTP_REFERER', '/') + f'#{photo_id}')
