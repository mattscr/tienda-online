from django import forms


CANTIDAD_OPCIONES_PRODUCTO = [(i, str(i)) for i in range(1, 26)]


class FormAgregarProductoCarrito(forms.Form):
    cantidad = forms.TypedChoiceField(choices=CANTIDAD_OPCIONES_PRODUCTO, coerce=int)
    actualizar = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)