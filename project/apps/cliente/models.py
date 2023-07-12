from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
<<<<<<< HEAD
    email=models.EmailField(max_length=50)
    pais_destino_id = models.ForeignKey(Pais, on_delete=models.PROTECT)
    especie = models.CharField(Arbol,max_length=50,null=True,blank=True)
    cantidad = models.IntegerField(Arbol,null=True,blank=True)
=======
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True,blank=True)
>>>>>>> 915a8d3395a8ce85b190ac19158f89b447093884

    def __str__(self):
        return f"{self.nombre} {self.apellido}"