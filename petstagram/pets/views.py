from django.shortcuts import render, redirect

from petstagram.pets.forms import PetAddForm
from petstagram.pets.models import Pet


# Create your views here.
def pet_add_page(request):
    form = PetAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context=context)


def pet_delete_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-delete-page.html')


def pet_edit_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-edit-page.html')


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)

    context = {
        'pet': pet,
    }

    return render(request, 'pets/pet-details-page.html', context)
