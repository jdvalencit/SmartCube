from django.db import models

# Create your models here.
class user(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    tfno = models.CharField(max_length=10)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
