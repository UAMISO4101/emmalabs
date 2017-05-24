from django.contrib import admin

# Register your models here.
from protocolo.models import Protocolo, ClasificacionProtocolo, Paso

class videoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    filter_horizontal = ('insumos',)

admin.site.register(Protocolo, videoAdmin)
admin.site.register(ClasificacionProtocolo)
admin.site.register(Paso)