from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Arbol(models.Model):
    # Define los campos de tu modelo
    especie = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.especie} {self.cantidad}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True,blank=True)
    especie = models.CharField(Arbol,max_length=100,null=True,blank=True)
    cantidad = models.IntegerField(Arbol,null=True,blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
