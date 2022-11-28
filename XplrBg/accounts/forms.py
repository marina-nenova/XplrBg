from cloudinary.forms import CloudinaryFileField
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from XplrBg.accounts.models import UserProfile
from XplrBg.core.mixins.form_mixins import SetFieldsClassFormMixin

UserModel = get_user_model()


class UserRegistrationForm(SetFieldsClassFormMixin, UserCreationForm):
    error_messages = {
        'password_mismatch': "The passwords don't match",
    }

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')
        error_messages = {
            UserModel.USERNAME_FIELD: {
                'unique': 'User with this email already exists',
            },
        }
        labels = {
            UserModel.USERNAME_FIELD: 'Email address',
            'password1': 'Password',
            'password2': 'Repeat Password',
        }



class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': ' form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': ' form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            if not UserModel.objects.filter(email=username):
                raise forms.ValidationError("Invalid username")

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Incorrect password")

        return super().clean()


class ProfileEditForm(SetFieldsClassFormMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image', 'first_name', 'last_name', 'lives_at')

    profile_image = CloudinaryFileField(
        options={
            'use_filename': True,
            'folder': 'XplrBg/Profiles/Images',
            'crop': 'limit', 'width': 300, 'height': 300,
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].required = False
