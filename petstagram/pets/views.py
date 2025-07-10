from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.photos.services import annotate_photos_with_likes


class AddPetView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class DeletePetView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('home-page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        obj = self.get_object()
        data = model_to_dict(obj)
        kwargs['initial'] = data

        return kwargs

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EditPetView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }
        )


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        photos = context['pet'].photo_set.all()
        annotate_photos_with_likes(photos, self.request.user)

        context['photos'] = photos

        return context
