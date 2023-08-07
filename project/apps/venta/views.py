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
    return render (request,"venta/index.html")

class VendedorList(ListView):
    model=models.Vendedor

class VendedorCreate(CreateView):
    model=models.Vendedor
    form_class= forms.VendedorForm
    success_url = reverse_lazy("venta:vendedor_list")

class VendedorDetail(DetailView):
    model=models.Vendedor

class VendedorUpdate(UpdateView):
    model=models.Vendedor
    form_class= forms.VendedorForm
    success_url = reverse_lazy("venta:vendedor_list")

class VendedorDelete(DeleteView):
    model=models.Vendedor
    success_url = reverse_lazy("venta:vendedor_list")

#List
class VentaList(ListView):
    model=models.Venta
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta=self.request.GET.get("consulta")
            object_list=models.Venta.objects.filter(nombre__icontains=consulta)
        else:
            object_list=models.Venta.objects.all()
        return object_list


#Create
class VentaCreate(CreateView):
    model=models.Venta
    form_class=forms.VentaForm
    succes_url=reverse_lazy("venta:venta_list")

#Detail
class VentaDetail(DetailView):
    model=models.Venta
    
#update
class VentaUpdate(UpdateView):
    model=models.Venta
    form_class=forms.VentaForm
    succes_url=reverse_lazy("venta:venta_list")

#Delete
class VentaDelete(DeleteView):
    model=models.Venta
    succes_url=reverse_lazy("venta:venta_list")