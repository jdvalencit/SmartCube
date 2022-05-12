from django.shortcuts import render
from gestionContenedores.models import contenedor as contenedor_model
from gestionUsuarios.forms import formularioInsertContenedor, formularioUpdateContenedor
from django.views import View
import requests
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
    if request.method=="GET": 
        id_update = request.GET["id"]
        lista = contenedor_model.objects.filter(id=id_update).update(status=False)
        
    return render(request, "contenedor_eliminado.html")

def chart(request):
    labels = []
    proximidad = []
    peso=[]

    r = requests.get('https://api.thingspeak.com/channels/1684778/feeds.json?api_key=51HH5MGDUL77VAV1')
    jsonData = r.json()

    for d in jsonData["feeds"]:
        proximidad.append(int(d["field1"]))
        peso.append(int(d["field2"]))
        sp = d["created_at"][11:-4].split(":")
        labels.append(str(int(sp[0])-5)+":"+sp[1])
        
    data = {"labels":labels,"proximidad":proximidad,"peso":peso}
    return render(request,'chart.html',{"data":data})

    