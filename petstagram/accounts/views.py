from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView

from petstagram.accounts.forms import AppUserCreationForm, AppUserAuthenticationForm, ProfileEditForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class AppUserLoginView(LoginView):
    form_class = AppUserAuthenticationForm
    template_name = 'accounts/login-page.html'


class AppUserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


def show_profile_details(request, pk):
    user = get_object_or_404(UserModel, pk=pk)
    pets = user.pets.all()
    total_likes = 0
    for photo in user.photos.all():
        for like in photo.likes.all():
            total_likes += 1

    context = {
        'user': user,
        'total_likes': total_likes,
        'pets': pets,
    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, 'accounts/profile-delete-page.html')
