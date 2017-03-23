from django.db import models

from insumo.models import Insumo

class Protocolo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    insumos = models.ManyToManyField(Insumo)


