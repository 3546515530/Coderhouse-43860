from django import forms
from .import models
class VendedorForm(forms.ModelForm):
    class Meta:
        model=models.Vendedor
        fields="__all__"

class VentaForm(forms.ModelForm):
    class Meta:
        model=models.Venta
        fields="__all__"
