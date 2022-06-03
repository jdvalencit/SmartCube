"""SmartCube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionUsuarios import views
from gestionContenedores import views as con_views
from contenido import views as contenido_views
from autenticacion import views as auth_views
#from django.contrib.auth.views import login,logout_then_login

urlpatterns = [
    path('',views.home, name="Home"),
    path('admin/', admin.site.urls),
    path('home/', views.home, name="Home"),
    path('contenedor/', con_views.contenedor, name="Cont"),
    path('insert_contenedor/', con_views.insert_contenedor),
    path('update_contenedor/', con_views.update_contenedor),
    path('delete_contenedor/', con_views.delete_contenedor),
    path('chart/', con_views.chart),
    path('contacto/',contenido_views.contacto,name="Contacto"),
    path('quienes_somos/',contenido_views.quienes_somos, name="Quienes"),
    path('servicios/',contenido_views.servicios, name="Servicios"),
    path('acerca_de/',contenido_views.acerca_de, name="Acerca"),
    path('autenticacion/',auth_views.Registro.as_view(),name="Autenticacion"),
    path('logout/',auth_views.cerrar_sesion, name="Logout"),
    path('login/',auth_views.iniciar_sesion, name="Login"),
    path('accounts/login/',auth_views.iniciar_sesion, name="Login"),

]
