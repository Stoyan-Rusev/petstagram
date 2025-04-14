from django import forms

from petstagram.pets.models import Pet


class PetAddForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'personal_photo', 'date_of_birth']

