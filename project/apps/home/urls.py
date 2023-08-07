from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import home
from .import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView



app_name="Home"
urlpatterns = [
    
    path("",views.home,name="home"),
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="Home/logout.html"), name="logout"),
    path('about/', TemplateView.as_view(template_name="home/about.html"),name="about"),
    path('register/', views.register,name="register"),
    path('tipo1_card_detalle/', TemplateView.as_view(template_name="Home/tipo1_card_detalle.html"),name="tipo1_card_detalle"),
    path('tipo2_card_detalle/', TemplateView.as_view(template_name="Home/tipo2_card_detalle.html"),name="tipo2_card_detalle"),
    path('tipo3_card_detalle/', TemplateView.as_view(template_name="Home/tipo3_card_detalle.html"),name="tipo3_card_detalle"),
    path('tipo4_card_detalle/', TemplateView.as_view(template_name="Home/tipo4_card_detalle.html"),name="tipo4_card_detalle"),
    path('tipo5_card_detalle/', TemplateView.as_view(template_name="Home/tipo5_card_detalle.html"),name="tipo5_card_detalle"),


]
urlpatterns += staticfiles_urlpatterns() #Permite llamar los archivos estaticos desde html