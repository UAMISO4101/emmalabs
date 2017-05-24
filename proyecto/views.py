# coding=utf-8
from django.shortcuts import render

import usuario.views as UsuarioView
from usuario.models import Usuario
from .models import Proyecto


def proyectos(request):
    # Inicializar variables
    lista_proyectos = []
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if request.user.is_authenticated:
        # Cargar los proyectos del usuario ha iniciado sesión
        lista_proyectos = Proyecto.objects.filter(asistentes__user__usuario=usuario_parametro.id)

    context = {
        'lista_proyectos': lista_proyectos,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'proyectos.html', context)
