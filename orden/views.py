from django.shortcuts import render

import usuario.views as UsuarioView
from usuario.models import Usuario
from .models import Orden


def ordenes(request):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    lista_ordenes = Orden.objects.all()

    context = {
        'lista_ordenes': lista_ordenes,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'ordenes.html', context)


def aprobar_orden(request, id):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    orden = Orden.objects.get(id=id)
    orden.estado = 1
    orden.save()

    orden = Orden.objects.get(id=id)

    context = {
        'orden': orden,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'detalle_orden.html', context)


def detalleOrden(request, id):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    orden = Orden.objects.get(id=id)

    context = {
        'orden': orden,
        'usuario_parametro': usuario_parametro,
        'lista_menu': lista_menu,
    }

    return render(request, 'detalle_orden.html', context)
