from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
<<<<<<< HEAD
        fields=["nombre","apellido","nacimiento","email","pais_destino_id","especie","cantidad"]

=======
        fields=["nombre","apellido","nacimiento","pais_destino_id","especie","cantidad","email"]
>>>>>>> 915a8d3395a8ce85b190ac19158f89b447093884
