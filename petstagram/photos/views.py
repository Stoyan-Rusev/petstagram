from django.shortcuts import render, get_object_or_404, redirect

from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context=context)


def photo_details(request, pk: int):
    photo = get_object_or_404(Photo, pk=pk)
    likes = photo.likes.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request):
    return render(request, 'photos/photo-edit-page.html')
