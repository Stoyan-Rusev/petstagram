from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', views.AppUserLogoutView.as_view(), name='logout'),
    path('delete_confirm/', views.delete_confirm, name='delete-confirm'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetails.as_view(), name='profile-details'),
        path('edit/', views.EditProfileView.as_view(), name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ]))
]
