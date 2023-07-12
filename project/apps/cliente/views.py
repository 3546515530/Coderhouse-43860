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


def crear_cliente(request: HttpRequest)-> HttpResponse:
    if request.method=="POST":
        form=ClienteForm(request.POST) #Guarda lo que cargo el usuario
        if Cliente==None:
            pass
        else:
            if form.is_valid():
                form.save()
                return redirect("cliente:home")

    else: #request.method="GET"
        form=ClienteForm() #Muestra campos para que el usuario cargue datos
        
    return render(request,"cliente/crear.html",{"form":form})


def crear_clientes(request):
    p1=Pais(nombre="Argentina")
    p2=Pais(nombre="Chile")
    p3=Pais(nombre="Brasil")
    p1.save()
    p2.save()
    p3.save()

    e1=Arbol(especie="Paraíso")
    e2=Arbol(especie="Algarrobo")
    e3=Arbol(especie="Sauce")
    e1.save()
    e2.save()
    e3.save()


    p1=Pais(nombre="Argentina")
    p2=Pais(nombre="Chile")
    p3=Pais(nombre="Brasil")
    p1.save()
    p2.save()
    p3.save()

    c1=Cliente(nombre="Rocio", apellido="Ruiseñor",nacimiento=date(2015,1,1),pais_destino_id=p1,especie=e1,cantidad=4, email="aa@gmail.com")
    c2=Cliente(nombre="Gabriela", apellido="Arreguiz",nacimiento=date(2005,2,2),pais_destino_id=p2,especie=e1,cantidad=5, email="bb@gmail.com")
    c3=Cliente(nombre="Macarena", apellido="Lito",nacimiento=date(1990,1,1),pais_destino_id=p3, especie=e2,cantidad=15, email="cc@gmail.com")
    c4=Cliente(nombre="Anabella", apellido="Homann",nacimiento=date(2005,1,1),pais_destino_id=None,especie=e3,cantidad=6,email="dd@gmail.com")
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
            return redirect("cliente:home")
            
    else: #request.method="GET"
        form=ClienteForm() #Muestra campos para que el usuario cargue datos

    return render(request,"cliente/crear.html",{"form":form})



def busqueda(request: HttpRequest)-> HttpResponse:
       
        #Clientes que quieran plantar Algarrobos
        cliente_arbol_especie=Cliente.objects.filter(arbol__especie__contains="Algarrobo")
        
        #Clientes que quieran plantar Cantidad
        cliente_arbol_cantidad=Cliente.objects.filter(arbol__cantidad__contains=15)
 
        contexto={ 
            "clientes_arbol_especie" : cliente_arbol_especie,
            "clientes_arbol_cantidad" : cliente_arbol_cantidad,
            }
        return render(request,"cliente/search.html",contexto)
