from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from gestionContenedores.models import contenedor as contenedor_model
from gestionUsuarios.forms import formularioInsertContenedor

# Create your views here.
def contenedor(request):
    return render(request,"contenedor.html")

def insert_contenedor(request):
    
    if request.method=="POST": 
        
        form_insert = formularioInsertContenedor(request.POST)

        if form_insert.is_valid():

            formdata = form_insert.cleaned_data
            contenedor = contenedor_model.objects.create(status=formdata['status'], tipo=formdata['tipo'], organizacion=formdata['organizacion'])
            return render(request, "contenedor_creado.html")

    else:
        form_insert = formularioInsertContenedor()

        return render(request, "insert_contenedor.html",{"form":form_insert})

def delete_contenedor(request):
    
    if request.method=="POST": 
        
        form_insert = formularioInsertContenedor(request.POST)

        if form_insert.is_valid():

            formdata = form_insert.cleaned_data
            contenedor = contenedor_model.objects.create(status=formdata['status'], tipo=formdata['tipo'], organizacion=formdata['organizacion'])
            return render(request, "contenedor_creado.html")

    else:
        form_insert = formularioInsertContenedor()

        return render(request, "insert_contenedor.html",{"form":form_insert})