from django.db import models

from usuario.models import Usuario


class Maquina(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)


class PrestamoMaquina(models.Model):
    maquina = models.ForeignKey(Maquina)
    usuario = models.ForeignKey(Usuario)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
