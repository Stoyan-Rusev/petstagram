from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from pyperclip import copy

from petstagram.common.forms import AddCommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


class HomeView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_text = ''
        search_form = SearchForm(self.request.GET)

        if search_form.is_valid():
            search_text = search_form.cleaned_data['search_text']

        context['search_form'] = search_form
        context['search_text'] = search_text
        context['comment_form'] = AddCommentForm(self.request.POST or None)

        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')
        search_text = self.request.GET.get('search_text')

        if search_text:
            queryset = queryset.filter(tagged_pets__name__icontains=search_text)

        return queryset


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
