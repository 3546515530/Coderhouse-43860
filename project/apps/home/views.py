
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http.request import HttpRequest
from django.http import HttpResponse
from .import forms

# Create your views here.
def home(request):
    return render (request,"home/index.html")

def login_request(request:HttpRequest)->HttpResponse:
    if request.method=="POST":
        form=forms.CustomAuthentificationForm(request,request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            user=authenticate(username=usuario,password=contraseña)
            if user is not None: #Hay algo
                login(request,user)
                return render(request,"home/index.html", {"mensaje":"Se inició sesion correctamente"})

    else:
        form=forms.CustomAuthentificationForm
    return render(request,"home/login.html",{"form":form})
