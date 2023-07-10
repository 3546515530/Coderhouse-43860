from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("home.urls")),
    path("cliente/",include("cliente.urls")),
    path("producto/",include("producto.urls")),
    path("nosotros/",include("nosotros.urls")),

]