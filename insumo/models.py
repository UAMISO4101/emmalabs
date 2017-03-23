from django.db import models

# Create your models here.
class Insumo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
