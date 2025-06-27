from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_and_time_of_production']),
        ]
        ordering = ['-date_and_time_of_production']

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
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='comments',
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='likes',
    )
