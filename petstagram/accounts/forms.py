from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password'
            })
        }


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


# class ProfileChangeForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user', )
