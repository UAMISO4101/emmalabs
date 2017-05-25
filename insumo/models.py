from django.db import models

# Create your models here.
class Insumo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    unidades = models.CharField(max_length=20, default="Unidades")

    def __str__(self):
        return '{}'.format(self.nombre)