from django.shortcuts import render, get_object_or_404, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
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

    return render(request, 'photos/photo-add-page.html', context)


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


def edit_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('photo-details', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('home-page')
