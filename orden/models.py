from django.db import models
from datetime import datetime
# Create your models here.
from solicitud.models import Solicitud


class Orden(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    fecha_orden = models.DateField(default=datetime.now, blank=True)
    solicitud = models.ForeignKey(Solicitud, related_name='solicitud', null=True)