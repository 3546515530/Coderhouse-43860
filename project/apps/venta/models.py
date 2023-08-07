from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.utils import timezone

# Create your models here.
class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return self.usuario.username



class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("producto.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_venta",)

    def clean(self):
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("La cantidad vendida no puede ser mayor a la cantidad disponible")

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.vendedor}|{self.producto}|${self.precio_total}"

