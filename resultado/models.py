from django.db import models
from experimento.models import Experimento
from protocolo.models import Protocolo
from proyecto.models import Proyecto

class Resultado(models.Model):
    detalle_resultado = models.CharField(max_length=50, blank=True, null=True)
    satisfactorio = models.BooleanField()
    observaciones = models.CharField(max_length=50, blank=True, null=True)
    fecha_resultado = models.DateTimeField(blank=True, null=True)
    proyecto = models.OneToOneField(Proyecto, related_name="proyecto")
    experimento = models.OneToOneField(Experimento, related_name="experimento")
    protocolo = models.OneToOneField(Protocolo, related_name="protocolo")