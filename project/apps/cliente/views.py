from django.shortcuts import render, redirect
from .models import Cliente, Pais, Arbol
from .forms import ClienteForm
from django.http import HttpRequest,HttpResponse
from datetime import date


# Create your views here.
def home(request):
    clientes_registros=Cliente.objects.all()
    contexto={"clientes": clientes_registros}
    return render (request,"cliente/index.html",contexto)


def crear_clientes(request):
    
    e1=Arbol(especie="Paraiso")
    e2=Arbol(especie="Algarrobo")
    e3=Arbol(especie="Sauce")
    e1.save()
    e2.save()
    e3.save()

    p1=Pais(nombre="Peru")
    p2=Pais(nombre="Mexico")
    p3=Pais(nombre="El salvador")
    p1.save()
    p2.save()
    p3.save()

    c1=Cliente(nombre="Rocio", apellido="Ruiseñor",nacimiento=date(2015,1,1),pais_origen_id=p1,especie=e1,cantidad=4, email="aa@gmail.com")
    c2=Cliente(nombre="Gabriela", apellido="Arreguiz",nacimiento=date(2005,2,2),pais_origen_id=p2,especie=e1,cantidad=5, email="bb@gmail.com")
    c3=Cliente(nombre="Macarena", apellido="Lito",nacimiento=date(1990,1,1),pais_origen_id=p3, especie=e3,cantidad=15, email="cc@gmail.com")
    c4=Cliente(nombre="Anabella", apellido="Homann",nacimiento=date(2005,1,1),pais_origen_id=None,especie=e2,cantidad=6,email="dd@gmail.com")
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:home")

def crear_cliente(request: HttpRequest)-> HttpResponse:
    if request.method=="POST":
        form=ClienteForm(request.POST) #Guarda lo que cargo el usuario
        if form.is_valid():
            form.save()
            print("Pedido registrado con exito")
            print("Te enviamos un correo con el detalle de tu pedido, gracias por ayudarnos!")
            return redirect("cliente:home")
            
    else: #request.method="GET"
        form=ClienteForm() #Muestra campos para que el usuario cargue datos

    return render(request,"cliente/crear.html",{"form":form})

def busqueda(request):
    #Busqueda por nobre que contenga "dana"
    cliente_nombre= Cliente.objects.filter(nombre__contains="dana")
    
    #Fechas mayores al 2000
    cliente_nacimiento=Cliente.objects.filter(nacimiento__gt=date(2000,1,1))
    
    #Fechas sin pais de origen
    cliente_pais=Cliente.objects.filter(pais_destino_id=None)
    
    #Clientes que quieran plantar Algarrobos
    cliente_especie=Cliente.objects.filter(especie="Algarrobo")

    contexto={
        "clientes_nombre" : cliente_nombre,
        "clientes_nacimiento" : cliente_nacimiento,
        "clientes_pais" : cliente_pais,
        "clientes_especie" : cliente_especie,
        }
    return render(request,"cliente/search.html",contexto)