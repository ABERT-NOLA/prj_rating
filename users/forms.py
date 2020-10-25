from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=150)


    class Meta:
        model = User
        fields = ['username','email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField()

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'contact', 'company']