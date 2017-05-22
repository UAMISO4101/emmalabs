from django.contrib import admin

# Register your models here.
from protocolo.models import Protocolo, ClasificacionProtocolo, Paso, ComentarioProtocolo

admin.site.register(Protocolo)
admin.site.register(ClasificacionProtocolo)
admin.site.register(Paso)
admin.site.register(ComentarioProtocolo)