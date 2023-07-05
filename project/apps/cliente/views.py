from django.shortcuts import render, redirect
from .models import Cliente, Pais
# Create your views here.
def home(request):
    clientes_registros=Cliente.objects.all()
    contexto={"clientes": clientes_registros}
    return render (request,"cliente/index.html",contexto)
def crear_clientes(request):
    from datetime import date
    p1=Pais(nombre="Peru")
    p2=Pais(nombre="Mexico")
    p3=Pais(nombre="El salvador")
    p1.save()
    p2.save()
    p3.save()
    c1=Cliente(nombre="Almendra", apellido="Ruiseñor",nacimiento=date(2015,1,1),pais_origen_id=p1)
    c2=Cliente(nombre="Giordana", apellido="Tapelo",nacimiento=date(2005,2,2),pais_origen_id=p2)
    c3=Cliente(nombre="Macarena", apellido="Lito",nacimiento=date(1990,1,1),pais_origen_id=p3)
    c4=Cliente(nombre="Jhiordana", apellido="Perez",nacimiento=date(2005,1,1),pais_origen_id=None)
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:home")