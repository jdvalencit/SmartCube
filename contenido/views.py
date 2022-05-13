from django.shortcuts import render
# Create your views here.

def contacto(request):
    return render(request, "contacto.html")

def quienes_somos(request):
    return render(request,"quienes_somos.html")

def servicios(request):
    return render(request,"servicios.html")

def acerca_de(request):
    return render(request,"acerca_de.html")