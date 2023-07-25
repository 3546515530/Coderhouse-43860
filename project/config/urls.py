from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("home.urls")),
    path("cliente/",include("cliente.urls")),
    path("producto/",include("producto.urls")),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)