from django.contrib import admin
from .models import Solicitud
from .models import TipoSolicitud

# Adicionar modelo Solicitud al administrador de Django
admin.site.register(Solicitud)
admin.site.register(TipoSolicitud)