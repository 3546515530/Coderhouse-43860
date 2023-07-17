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



]
urlpatterns += staticfiles_urlpatterns() #Permite llamar los archivos estaticos desde html