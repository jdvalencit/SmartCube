from inspect import formatannotation
from django import forms

class formularioRegistro (forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    usuario = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class formularioInsertContenedor (forms.Form):
    status = forms.BooleanField()
    tipo = forms.CharField(max_length=50)
    organizacion = forms.CharField(max_length=50)
    
class formularioUpdateContenedor (forms.Form):
    tipo = forms.CharField(max_length=50)
    organizacion = forms.CharField(max_length=50)
    
