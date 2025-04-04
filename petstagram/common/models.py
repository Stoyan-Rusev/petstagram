from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    comment_text = models.CharField(
        max_length=300
    )
    date_and_time_of_production = models.DateTimeField(
        auto_now_add=True
    )
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
        related_name='likes'
    )
