from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Room

# Форма для регистрации
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'description', 'price_night', 'image']