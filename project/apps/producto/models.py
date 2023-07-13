
from django.db import models

class ProductoCategoria(models.Model):

    """Categorías de productos """

    nombre = models.CharField(max_length=200, unique=True)

    descripcion = models.CharField(

        max_length=250, null=True, blank=True, verbose_name="descripción")

 

    def __str__(self):

        """Representa una instancia de la clase como una cadena de texto"""

        return self.nombre

 

    class Meta:

        verbose_name = "categoría de productos"

        verbose_name_plural = "categorías de productos"