from django.contrib import admin

# Register your models here.
from usuario.models import Usuario, Rol, MenuPorRol

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(MenuPorRol)
