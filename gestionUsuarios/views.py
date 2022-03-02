from django.http import HttpResponse
from django.shortcuts import render
from gestionUsuarios.models import user

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        form_user=request.POST["username"]
        form_pass=request.POST["password"]

        try:
            usuario = user.objects.get(usuario=form_user)
        except:
            return render(request,"fallo.html")
        
        if usuario.password == form_pass:
            return render(request,"sesion.html")
        else:
            return render(request,"fallo.html")

    return render(request,"login.html")

def signup(request):
    
    if request.method=="POST":
        form_nombre=request.POST["nombre"]
        form_direccion=request.POST["direccion"]
        form_email=request.POST["email"]
        form_tfno=request.POST["telefono"]
        form_usuario=request.POST["username"]
        form_pass=request.POST["password"]
        usuario = user.objects.create(nombre=form_nombre, direccion=form_direccion, email=form_email, tfno=form_tfno, usuario=form_usuario,password=form_pass)
        
        return render(request,"usuario_creado.html")

    return render(request,"signup.html")

