from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('like_photo/<int:photo_id>', views.like_unlike_photo, name='like-photo'),
    path('share/<int:pk>', views.copy_link_to_clipboard, name='share'),
    path('add_comment/<int:photo_id>', views.add_comment, name='add-comment'),
]
