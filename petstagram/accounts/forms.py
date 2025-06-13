from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.EmailInput(),
        label="Email",
    )

    class Meta:
        model = UserModel
        fields = '__all__'

# class ProfileChangeForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user', )
