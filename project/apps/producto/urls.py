from django.urls import path
#from .views import index
from .import views
from django.views.generic import TemplateView
app_name="producto"
#Producto categoria
urlpatterns = [
    path("",views.index,name="home"),
    # path("",TemplateView.as_view(template_name="producto/index.html"),name="home"),
    # path("productocategoria/list/",views.productocategoria_list,name="productocategoria_list"),
    path("productocategoria/list/",views.ProductoCategoriaList.as_view(),name="productocategoria_list"),
    # path("productocategoria/create/",views.productocategoria_create,name="productocategoria_create"),
    path("productocategoria/create/",views.ProductoCategoriaCreate.as_view(),name="productocategoria_create"),
    # path("productocategoria/detail/<int:pk>",views.productocategoria_detail,name="productocategoria_detail"),
    path("productocategoria/detail/<int:pk>",views.ProductoCategoriaDetail.as_view(),name="productocategoria_detail"),
    # path("productocategoria/update/<int:pk>",views.productocategoria_update,name="productocategoria_update"),
    path("productocategoria/update/<int:pk>",views.ProductoCategoriaUpdate.as_view(),name="productocategoria_update"),
    # path("productocategoria/delete/<int:pk>",views.productocategoria_delete,name="productocategoria_delete"),
    path("productocategoria/delete/<int:pk>",views.ProductoCategoriaDelete.as_view(),name="productocategoria_delete"),

]

#Producto
#con el += Adiciono al listado anterior,para evitar repetir codigo.
urlpatterns += [
    path("",views.index,name="home"),
    path("producto/list/",views.ProductoList.as_view(),name="producto_list"),
    path("producto/create/",views.ProductoCreate.as_view(),name="producto_create"),
    path("producto/detail/<int:pk>",views.ProductoDetail.as_view(),name="producto_detail"),
    path("producto/update/<int:pk>",views.ProductoUpdate.as_view(),name="producto_update"),
    path("producto/delete/<int:pk>",views.ProductoDelete.as_view(),name="producto_delete"),

]