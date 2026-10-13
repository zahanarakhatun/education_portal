from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel

class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email'] # password UserCreationForm auto dey