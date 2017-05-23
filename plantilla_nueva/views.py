from django.shortcuts import render

import usuario.views as UsuarioView
from proyecto.models import Proyecto, Experimento
from solicitud.models import Solicitud
from maquina.models import PrestamoMaquina
from usuario.models import LoginForm
from usuario.models import Usuario


def index(request):
    form_login = LoginForm()
    lista_menu = []
    usuario_parametro = ''
    usuario_proyectos = ''
    usuario_experimentos = ''
    usuario_solicitudes = ''
    usuario_maquinas = ''

    if request.user.is_authenticated:
        # Crear el menu del usuario
        lista_menu = UsuarioView.crearMenu(request.user)
        # Cargar el usuario activo
        usuario_parametro = Usuario.objects.get(user_id=request.user.id)

        # Cargar informacion del dashboard
        usuario_proyectos = len(Proyecto.objects.filter(asistentes__user=request.user.id))
        usuario_experimentos = len(Experimento.objects.filter(
            experimento__proyecto_id__in=Proyecto.objects.filter(asistentes__user=request.user.id)))
        usuario_solicitudes = len(Solicitud.objects.filter(usuario_creador=request.user.id))
        usuario_maquinas = len(PrestamoMaquina.objects.filter(usuario=request.user.id))

    context = {'form_login': form_login,
               'lista_menu': lista_menu,
               'usuario_parametro': usuario_parametro,
               'usuario_proyectos': usuario_proyectos,
               'usuario_experimentos': usuario_experimentos,
               'usuario_solicitudes': usuario_solicitudes,
               'usuario_maquinas': usuario_maquinas
               }

    return render(request, 'index.html', context)
