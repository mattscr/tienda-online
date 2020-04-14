from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    Nombre = forms.CharField(max_length=30, required=False, help_text='Optional')
    Apellido = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'Nombre', 
            'Apellido', 
            'email', 
            'password1', 
            'password2', 
            ]