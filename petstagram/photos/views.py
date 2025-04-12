from django.shortcuts import render, get_object_or_404

from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


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
