from django.db import models
from datetime import datetime
from protocolo.models import Protocolo

class Experimento(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    fecha_resultado = models.DateField(default=datetime.now, blank=True)
    protocolos = models.ManyToManyField(Protocolo)