from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from petstagram.common.forms import AddCommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo
from petstagram.photos.services import annotate_photos_with_likes


class PhotoAddView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhotoEditView(LoginRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        annotate_photos_with_likes([self.object], self.request.user)

        context['likes'] = self.object.likes.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = AddCommentForm()

        return context


@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if photo.user != request.user:
        raise Http404()

    photo.delete()
    return redirect('home-page')