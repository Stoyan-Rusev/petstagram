from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

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


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pets'] = self.object.pets.all()
        context['total_likes'] = sum(1 for photo in self.object.photos.all() for like in photo.likes.all())

        return context


@login_required
def delete_confirm(request):
    return render(request, 'accounts/profile-delete-page.html')


@require_POST
@login_required
def delete_profile(request, pk):
    if request.user.pk == pk:
        request.user.delete()
    return redirect('home-page')
