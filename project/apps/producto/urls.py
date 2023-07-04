from django.urls import path
from .views import home
app_name="producto"
urlpatterns = [

    path("",home,name="home"),
]
