from django.db import models

# Create your models here.
from usuario.models import Usuario

class Solicitud(models.Model):
    titulo = models.CharField(max_length=40, blank=True, null=True)
    texto = models.CharField(max_length=255, blank=True, null=True)
    asistente = models.ForeignKey(Usuario, related_name='asistente', null=True)
    cientifico = models.ForeignKey(Usuario, related_name='cientifico', null=True)