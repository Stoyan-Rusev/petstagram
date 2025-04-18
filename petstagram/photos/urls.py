from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit'),
        path('delete/', views.delete_photo, name='photo-delete'),
    ])),

]
