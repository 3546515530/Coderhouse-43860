from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=["nombre","apellido","nacimiento","email","pais_destino_id","arbol"]

