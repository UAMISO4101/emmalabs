# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from insumo.models import Insumo


class Paso(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    entradas = models.ManyToManyField(Insumo, related_name="entradas")
    salidas = models.ManyToManyField(Insumo, related_name="salidas")


class ClasificacionProtocolo(models.Model):
    nombre_clasificacion = models.CharField(max_length=50, default="Sin clasificación")


class Protocolo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    version = models.FloatField(default=1.0)
    pasos = models.ManyToManyField(Paso, related_name="pasos")
    fecha_creacion = models.DateField(default=datetime.now, blank=True, null=False)
    codigo = models.CharField(max_length=10, default="PRO-000", blank=True , null=False)
    clasificacion = models.ForeignKey(ClasificacionProtocolo, related_name="clasificacion")


