from django.db import models

# Create your models here.
from experimento.models import Experimento
from usuario.models import Usuario


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    experimentos = models.ManyToManyField(Experimento)
    asistentes = models.ManyToManyField(Usuario)