from django.contrib import admin

# Register your models here.
from maquina.models import Maquina, PrestamoMaquina

admin.site.register(Maquina)
admin.site.register(PrestamoMaquina)