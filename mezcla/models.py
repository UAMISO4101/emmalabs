from django.db import models
from experimento.models import Experimento
from protocolo.models import Protocolo
from proyecto.models import Proyecto
from maquina.models import Maquina
from insumo.models import Insumo

class Mezcla(models.Model):
    resultado = models.CharField(max_length=50, blank=True, null=True)
    insumos = models.ManyToManyField(Insumo, related_name="insumos_m")
    maquina = models.ForeignKey(Maquina, related_name="maquina")
    proyecto = models.ForeignKey(Proyecto, related_name="proyecto")
    experimento = models.ForeignKey(Experimento, related_name="experimento")
    protocolo = models.ForeignKey(Protocolo, related_name="protocolo")