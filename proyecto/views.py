# coding=utf-8
from django.shortcuts import render
from usuario.models import Usuario
from .models import Proyecto


def proyectos(request):
    # Inicializar variables
    usuario_actual = request.user
    lista_proyectos = []

    if request.user.is_authenticated:
        print("Autenticado!")
        # Cargar los proyectos solo si el usuario ha iniciado sesión
        lista_proyectos = Proyecto.objects.filter(asistente__asistente__cientifico_id=usuario_actual.id)


    context = {'lista_proyectos': lista_proyectos}
    return render(request, 'proyectos.html', context)
