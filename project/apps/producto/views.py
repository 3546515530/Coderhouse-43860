from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView ,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .import models
from .import forms
#Importaciones para Login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
#PAGINA PRINCIPAL

@login_required #Decorador
def index(request):
    return render (request,"producto/index.html")

#LIST


# def productocategoria_list(request):
#     categorias=models.ProductoCategoria.objects.all()
#     context={"object_list":categorias}
#     return render (request,"producto/productocategoria_list.html",context)

class ProductoCategoriaList(ListView):
    model=models.ProductoCategoria


#CREATE
# def productocategoria_create(request):
#     if request.method == "POST":
#         form =forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:home")
#     else:
#         form=forms.ProductoCategoriaForm()
#     return render(request,"producto/productocategoria_form.html",{"form":form})

class ProductoCategoriaCreate(CreateView):
    model=models.ProductoCategoria
    form_class= forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

#DETALLE


# def productocategoria_detail(request,pk):
#     query=models.ProductoCategoria.objects.get(id=pk)
#     return render(request,"producto/productocategoria_detail.html",{"object":query})

class ProductoCategoriaDetail(DetailView):
    model=models.ProductoCategoria

    
#UPDATE

# def productocategoria_update(request,pk):
#     query=models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form =forms.ProductoCategoriaForm(request.POST, instance=query)#Actualiza sobre el mismo formulario que estamos editando, y no genera uno nuevo.
#         if form.is_valid():
#             form.save()
#             return redirect("producto:home")
#     else:
#         form=forms.ProductoCategoriaForm(instance=query) #Ve el usuario ya informacion ya cargada
#     return render(request,"producto/productocategoria_form.html",{"form":form})

class ProductoCategoriaUpdate(UpdateView):
    model=models.ProductoCategoria
    form_class= forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

#ELIMINAR
# def productocategoria_delete(request,pk):
#     query=models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return render(request,"producto/productocategoria_list.html")
#     return render(request,"producto/productocategoria_confirm_delete.html",{"object":query})

class ProductoCategoriaDelete(DeleteView):
    model=models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

#List
class ProductoList(ListView):
    model=models.Producto
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta=self.request.GET.get("consulta")
            object_list=models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list=models.Producto.objects.all()
        return object_list


#Create
class ProductoCreate(CreateView):
    model=models.Producto
    form_class=forms.ProductoForm
    succes_url=reverse_lazy("producto:producto_list")

#Detail
class ProductoDetail(DetailView):
    model=models.Producto
    
#update
class ProductoUpdate(UpdateView):
    model=models.Producto
    form_class=forms.ProductoForm
    succes_url=reverse_lazy("producto:producto_list")

#Delete
class ProductoDelete(DeleteView):
    model=models.Producto
succes_url=reverse_lazy("producto:producto_list")