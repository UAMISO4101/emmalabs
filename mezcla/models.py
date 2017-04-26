from django.db import models
from resultado.models import Resultado
from maquina.models import Maquina
from insumo.models import Insumo

class Mezcla(models.Model):
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    insumos = models.ManyToManyField(Insumo)
    maquina = models.ForeignKey(Maquina)
    resultado = models.ForeignKey(Resultado)