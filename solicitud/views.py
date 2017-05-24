from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import usuario.views as UsuarioView
from orden.forms import OrdenForm
from usuario.models import Usuario
from .forms import SolicitudForm
from .models import Solicitud


# Vista para crear una solicitud
def crear_solicitud(request):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        # Validar formulario
        if form.is_valid():
            solicitud = form.save(commit=False)
            # Se debe guardar el usuario creador
            solicitud.usuario_creador = Usuario.objects.get(user=request.user)
            # Guardar la solicitud
            solicitud.save()
            # Cargar mensaje de exito
            messages.add_message(request, messages.SUCCESS, 'La solicitud se ha creado correctamente')
            # Retornar a la pagina crearSolicitud
            return HttpResponseRedirect(reverse('crearSolicitud'))
        else:
            # Visualizar errores presentados
            print(form.errors)
    else:
        form = SolicitudForm()

    context = {
        'form': form,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'crearSolicitud.html', context)


def menu_solicitud(request):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)
    context = {
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
    }
    return render(request, 'menuSolicitud.html', context)


# Vista para listar las solicitudes del usuario
def listar_solicitudes(request):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)
    usuario = Usuario.objects.get(user=request.user)

    if usuario.rol_usuario.rol == "rol_asistente":
        # Se filtran las solicitudes por usuario creador
        lista_solicitudes = Solicitud.objects.filter(usuario_creador=usuario).order_by('-fecha_creacion')
    else:
        # Se filtran las solicitudes por usuario destino
        lista_solicitudes = Solicitud.objects.filter(usuario_destino=usuario).order_by('-fecha_creacion')

    context = {
        'lista_solicitudes': lista_solicitudes,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
    }
    return render(request, 'solicitudes.html', context)


def ver_Solicitud(request, id):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if (request.method == "POST" and 'btn_aprobarSol' in request.POST):
        form = OrdenForm(request.POST)
        # Validar formulario
        if form.is_valid():
            orden = form.save(commit=False)
            # Se debe guardar la solicitud referente a la orden de compra
            orden.solicitud = Solicitud.objects.get(id=id)
            # Guardar la orden de compra
            orden.save()
            # Actualizar el estado de la solicitud a aprobado
            solicitud = Solicitud.objects.get(id=id)
            solicitud.estado = "Aprobado"
            solicitud.respuesta = request.POST['respuestaAprobado']
            solicitud.save()
            # Retornar a la pagina crearSolicitud
            return HttpResponseRedirect(reverse('solicitudes'))
        else:
            # Visualizar errores presentados
            print(form.errors)

    # #Actualizar el estado de la solicitud a rechazado
    elif (request.method == "POST" and 'btn_rechazarSol' in request.POST):
        solicitud = Solicitud.objects.get(id=id)
        solicitud.estado = "Rechazado"
        solicitud.respuesta = request.POST['respuesta']
        solicitud.save()
        return HttpResponseRedirect(reverse('solicitudes'))

    # Mostrar estado formulario de la solicitud consultada
    else:
        usuario = Usuario.objects.get(user=request.user)
        solicitud = Solicitud.objects.get(id=id)
        if usuario.rol_usuario.rol != "rol_asistente" and solicitud.estado == "Pendiente":
            form = OrdenForm()
            context = {
                'solicitud': solicitud,
                'form': form,
                'lista_menu': lista_menu,
                'usuario_parametro': usuario_parametro,
            }
        else:
            context = {
                'solicitud': solicitud,
                'lista_menu': lista_menu,
                'usuario_parametro': usuario_parametro,
            }

    return render(request, 'verSolicitud.html', context)
