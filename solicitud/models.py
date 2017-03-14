from django.db import models

# Create your models here.
class Solicitud(models.Model):
    texto = models.CharField(max_length=255, blank=True, null=True)
    cientifico = models.CharField(max_length=30, blank=True, null=True)