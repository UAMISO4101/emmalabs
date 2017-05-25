# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from insumo.models import Insumo
from usuario.models import Usuario

class ClasificacionProtocolo(models.Model):
    nombre_clasificacion = models.CharField(max_length=50, default="Sin clasificacion")

    def __str__(self):
        return '{}'.format(self.nombre_clasificacion)

class Protocolo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=5000, blank=True, null=False)
    version = models.FloatField(default=1.0)
    insumos = models.ManyToManyField(Insumo, related_name="insumos")
    fecha_creacion = models.DateField(default=datetime.now, blank=True, null=False)
    codigo = models.CharField(max_length=10, blank=False, null=False)
    clasificacion = models.ForeignKey(ClasificacionProtocolo, related_name="clasificacion")
    observaciones = models.CharField(max_length=500, blank=True, null=False)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Paso(models.Model):
    descripcion = models.CharField(max_length=5000, blank=False, null=False)
    protocolo = models.ForeignKey(Protocolo, on_delete=models.CASCADE)

class ComentarioProtocolo(models.Model):
    texto = models.CharField(max_length=5000, blank=False, null=False)
    fecha_creacion = models.DateField(default=datetime.now, blank=True, null=False)
    protocolo = models.ForeignKey(Protocolo)
    usuario = models.ForeignKey(Usuario)
