from datetime import datetime

from django.db import models

from usuario.models import Usuario


# Modelo de solicitud
class Solicitud(models.Model):
    titulo = models.CharField(max_length=40, blank=True, null=True)
    texto = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField(default=datetime.now, blank=True)
    asistente = models.ForeignKey(Usuario, related_name='asistente', null=True)
    cientifico = models.ForeignKey(Usuario, related_name='cientifico', null=True)
