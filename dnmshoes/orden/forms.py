from django import forms
from .models import Orden


class FormCrearOrden(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['Nombre', 'Apellido', 'email', 'Direccion', 'Codigo_Postal', 'Ciudad']
