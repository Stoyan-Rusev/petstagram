from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('like_photo/<int:photo_id>', views.like_unlike_photo, name='like-photo'),
]
