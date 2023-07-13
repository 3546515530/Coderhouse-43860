from django.contrib import admin
from .import models

admin.site.site_title = "Productos"
#admin.site.register(models.ProductoCategoria)

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","descripcion",)
    list_filter = ("nombre",)
    search_fields = ("nombre","descripcion",)
    ordering = ("nombre",)
  
