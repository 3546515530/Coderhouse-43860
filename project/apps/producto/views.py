from django.shortcuts import render

# Create your views here.
def home(request):
    contexto={"aplicacion": "App Producto"}
    return render (request,"producto/index.html",contexto)