from django.contrib import admin

# Register your models here.
from protocolo.models import Protocolo, ClasificacionProtocolo, Paso

admin.site.register(Protocolo)
admin.site.register(ClasificacionProtocolo)
admin.site.register(Paso)