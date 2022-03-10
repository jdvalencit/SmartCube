from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from gestionContenedores.models import contenedor as contenedor_model
from gestionUsuarios.forms import formularioInsertContenedor, formularioUpdateContenedor
from django.views import View

# Create your views here.
def contenedor(request):
    
    lista = contenedor_model.objects.filter(status=True).order_by('id')
    
    return render(request,"contenedor.html",{"lista":lista})

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

def update_contenedor(request):

    if request.method=="POST": 
            
            form_update = formularioUpdateContenedor(request.POST)
            if form_update.is_valid(): 
                formdata = form_update.cleaned_data
                id_update = request.POST["id_form"]
                
                lista = contenedor_model.objects.filter(id=id_update).update(tipo=formdata['tipo'],organizacion=formdata['organizacion'])

            return render(request,"contenedor_actualizado.html")
    elif request.GET["id"]:
        id_update = request.GET["id"]

    form_update = formularioUpdateContenedor()
    return render(request, "update_contenedor.html",{"form":form_update,"id":id_update})

def delete_contenedor(request):

    return render(request, "insert_contenedor.html")


