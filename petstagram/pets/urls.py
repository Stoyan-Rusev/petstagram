from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.AddPetView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsView.as_view(), name='pet-details'),
        path('edit/', views.pet_edit_page, name='pet-edit'),
        path('delete/', views.pet_delete_page, name='pet-delete'),
    ])),
]
