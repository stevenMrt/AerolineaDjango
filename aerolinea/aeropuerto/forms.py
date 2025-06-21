from django import forms
from .models import Aeropuerto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AeropuertoForm(forms.ModelForm):
    class Meta:
        model=Aeropuerto
        fields='__all__'
        
class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2']