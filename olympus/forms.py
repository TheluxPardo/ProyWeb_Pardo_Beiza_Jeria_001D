
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reserva
from django.core.exceptions import ValidationError
# forms.py

class CustomUserCreationForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise ValidationError("El correo electrónico debe ser de Gmail.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if not any(char.isdigit() for char in username):
            raise ValidationError("El nombre de usuario debe contener al menos un número.")
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
#---------------------------------------
    
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.rut = self.cleaned_data['rut']
        if commit:
            user.save()
        return user



class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'servicio', 'fecha', 'hora', 'estado']