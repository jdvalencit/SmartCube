from django.db import models
# Create your models here.
class contenedor(models.Model):
    status = models.BooleanField()
    tipo = models.CharField(max_length=50)
    organizacion = models.CharField(max_length=50)
    