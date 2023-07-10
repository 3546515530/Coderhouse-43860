from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=["nombre","apellido","nacimiento","pais_destino_id","especie","cantidad","email"]