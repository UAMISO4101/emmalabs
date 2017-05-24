# coding=utf-8
import datetime
from django.shortcuts import render
import usuario.views as UsuarioView
from django.http import HttpResponseRedirect
from django.contrib import messages
from proyecto.forms import ProyectoForm
from usuario.models import Usuario
from .models import Proyecto
from django.urls import reverse


def proyectos(request):
    # Inicializar variables
    usuario_actual = Usuario.objects.get(user=request.user)
    usuario_parametro = Usuario.objects.get(user_id=usuario_actual.id)
    lista_proyectos = []
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)


    # if usuario_actual.is_authenticated:
    # Cargar los proyectos del usuario ha iniciado sesión
    if usuario_actual.rol_usuario == "rol_asistente":

        lista_proyectos = Proyecto.objects.filter(asistentes__user__usuario=usuario_parametro.id)
    else:
        lista_proyectos = Proyecto.objects.all()

    context = {
        'lista_proyectos': lista_proyectos,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'proyectos.html', context)

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        # Validar formulario
        if form.is_valid():
            proyecto = form.save(commit=False)
            # Se debe guardar el usuario creador
            proyecto.cientifico_asignado = Usuario.objects.get(user=request.user)
            # Guardar la solicitud
            proyecto.save()
            # Cargar mensaje de exito
            messages.add_message(request, messages.SUCCESS, 'El proyecto se ha creado correctamente')
            # Retornar a la pagina crearSolicitud
            return HttpResponseRedirect(reverse('crearProyecto'))
        else:
            # Visualizar errores presentados
            print(form.errors)
    else:
        form = ProyectoForm()

    return render(request, 'crearProyecto.html', {'form':form})