from django.shortcuts import render

# Create your views here.
def home(request):
    contexto={"aplicacion": "Vida verde"}
    return render (request,"nosotros/index.html",contexto)