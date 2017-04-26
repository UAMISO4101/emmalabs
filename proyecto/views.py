# coding=utf-8
from django.shortcuts import render
from usuario.models import Usuario
from .models import Proyecto


def proyectos(request):
    # Inicializar variables
    usuario_actual = request.user
    usuario_parametro = Usuario.objects.get(user_id=usuario_actual.id)
    lista_proyectos = []

    if usuario_actual.is_authenticated:
        # Cargar los proyectos del usuario ha iniciado sesión
        lista_proyectos = Proyecto.objects.filter(asistentes__user__usuario=usuario_parametro.id)

    context = {'lista_proyectos': lista_proyectos}
    
    return render(request, 'proyectos.html', context)
