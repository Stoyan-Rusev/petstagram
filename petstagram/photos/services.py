def annotate_photos_with_likes(photos, user):
    for photo in photos:
        photo.has_liked = photo.likes.filter(user=user).exists() if user.is_authenticated else False

    return photos
