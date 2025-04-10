from django.shortcuts import render, get_object_or_404

from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk: int):
    photo = get_object_or_404(Photo, pk=pk)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request):
    return render(request, 'photos/photo-edit-page.html')
