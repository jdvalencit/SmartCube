from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from gestionUsuarios.models import user
from gestionUsuarios.forms import formularioRegistro

# Create your views here.
def home(request):
    return render(request,"home.html")
