# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from insumo.models import Insumo


class ClasificacionProtocolo(models.Model):
    nombre_clasificacion = models.CharField(max_length=50, default="Sin clasificación")


class Protocolo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=5000, blank=True, null=False)
    version = models.FloatField(default=1.0)
    insumos = models.ManyToManyField(Insumo, related_name="insumos")
    fecha_creacion = models.DateField(default=datetime.now, blank=True, null=False)
    codigo = models.CharField(max_length=10, default="PRO-000", blank=True, null=False)
    clasificacion = models.ForeignKey(ClasificacionProtocolo, related_name="clasificacion")
