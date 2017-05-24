from datetime import datetime
from django.db import models

# Create your models here.
from experimento.models import Experimento
from usuario.models import Usuario


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateField(default=datetime.now, blank=True)
    cientifico_asignado = models.asistente = models.ForeignKey(Usuario, related_name='cientifico_asignado', null=True)
    experimentos = models.ManyToManyField(Experimento)
    asistentes = models.ManyToManyField(Usuario)