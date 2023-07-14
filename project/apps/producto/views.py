from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView ,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .import models
from .import forms
# Create your views here.
#PAGINA PRINCIPAL


# def index(request):
#     return render (request,"producto/index.html")

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