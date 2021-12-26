from django import forms # Para usar formularios de Django
from django.core import validators # Para usar validaciones
from django.contrib.auth.forms import UserCreationForm # Formulario por defecto
from django.contrib.auth.models import User # Para usar Modelo de usuario

# Clase que hereda de la clase UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        # Hacer que este formulario se base en el modelo User
        model = User
        # Definir campos que tendrá el formulario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']