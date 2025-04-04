from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.
def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos,
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





