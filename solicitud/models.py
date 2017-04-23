from datetime import datetime
from django.db import models
from usuario.models import Usuario

#Modelo de tipo de solicitud
class TipoSolicitud(models.Model):
    nombre = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)


# Obtener el id del usuario que esta actualmente logueado
def obtener_id_usuario():
    return 1

# Modelo de solicitud
class Solicitud(models.Model):
    titulo = models.CharField(max_length=40, blank=True, null=True)
    texto = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField(default=datetime.now, blank=True)
    tipo = models.ForeignKey(TipoSolicitud, related_name='Tipo', null=True)
    usuario_creador = models.ForeignKey(Usuario, related_name='asistente', null=True)
    usuario_destino = models.ForeignKey(Usuario, related_name='cientifico', null=True)
    respuesta = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=40, blank=True, default="Pendiente", null=True)