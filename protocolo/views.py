# -*- coding: utf-8 -*-

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import usuario.views as UsuarioView
from usuario.models import Usuario
from .forms import ProtocoloForm, CrearProtocoloForm, ActualizarProtocoloForm
from .models import Protocolo, Paso, ComentarioProtocolo


def buscar_protocolo_vista(request):
    # Inicializa listado de protocolos
    lista_protocolos = Protocolo.objects.all()
    # Bandera para mostrar/ocultar los resultados
    mostrar_resultados = False
    # Cargar el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        # Envia el formulario con los datos diligenciados por el usuario
        protocolo_form = ProtocoloForm(data=request.POST)

        # Validar si el formulario es correcto
        if protocolo_form.is_valid():
            mostrar_resultados = True
            # Aplicar criterios de busqueda

            lista_protocolos = Protocolo.objects.all()
            # Se aplican los filtros que el usuario digita
            if len(request.POST.get('codigo')) > 0:
                lista_protocolos = lista_protocolos.filter(codigo__contains=request.POST.get('codigo'))
            if request.POST.get('clasificacion') != '':
                lista_protocolos = lista_protocolos.filter(
                    clasificacion__nombre_clasificacion__contains=request.POST.get('clasificacion'))
            if request.POST.get('nombre') != '':
                lista_protocolos = lista_protocolos.filter(nombre__contains=request.POST.get('nombre'))




    else:  # Si el request es de tipo get
        # Inicializa formulario vacio
        protocolo_form = ProtocoloForm()

    context = {
        'lista_menu': lista_menu,
        'formProtocolo': protocolo_form,
        'lista_protocolos': lista_protocolos,
        'mostrar_resultados': mostrar_resultados,
        'usuario_parametro': usuario_parametro,
    }

    return render(request, 'buscarProtocolos.html', context)


def detalle_protocolo_vista(request, id_protocolo):
    if (request.method == "POST"):
        usuario_actual = request.user
        usuario = Usuario.objects.get(user_id=usuario_actual.id)
        comentario_nuevo = ComentarioProtocolo()
        comentario_nuevo.texto = request.POST['comentario_nuevo']
        comentario_nuevo.protocolo = Protocolo.objects.get(id=request.POST['id_protocolo'])
        comentario_nuevo.usuario = usuario
        comentario_nuevo.save()

    # Obtiene el objeto de referencia
    protocolo = Protocolo.objects.get(id=id_protocolo)
    # Traer los objetos relacionados
    lista_pasos = Paso.objects.filter(protocolo=id_protocolo)
    lista_insumos = protocolo.insumos.all()
    # Cargar el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)
    comentarios_protocolo = ComentarioProtocolo.objects.filter(protocolo=id_protocolo).order_by('id')

    # Subir la informacion al contexto
    context = {
        'protocolo': protocolo,
        'lista_pasos': lista_pasos,
        'lista_insumos': lista_insumos,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
        'comentarios_protocolo': comentarios_protocolo
    }

    return render(request, 'protocolos.html', context)


# Vista para crear un Protocolo
def crear_protocolo(request):
    if request.method == 'POST':
        form = CrearProtocoloForm(request.POST)
        # Validar formulario
        if form.is_valid():
            protocolo = form.save()
            # Guardar la protocolo
            protocolo.save()
            # Cargar mensaje de exito
            messages.add_message(request, messages.SUCCESS, 'El protocolo se ha creado correctamente')
            # Retornar a la pagina crearSolicitud
            return HttpResponseRedirect(reverse('crearProtocolo'))
        else:
            # Visualizar errores presentados
            print(form.errors)
    else:
        form = CrearProtocoloForm()

    return render(request, 'crearProtocolo.html', {'form': form})


def actualizar_protocolo(request, id_protocolo):
    # Cargar el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)
    # Obtiene el objeto de referencia
    protocolo = Protocolo.objects.get(id=id_protocolo)
    # Inicializar el formulario
    form_actualizar_protocolo = ActualizarProtocoloForm()

    if (request.method == "POST"):
        # Cargar datos del formulario
        form_actualizar_protocolo = ActualizarProtocoloForm(request.POST)
        # Validar formulario
        if form_actualizar_protocolo.is_valid():
            # Actualizar informacion del protocolo
            protocolo_actualizado = form_actualizar_protocolo.save()
            # Aumentar la version del protocolo
            protocolo_actualizado.version = protocolo.version + 0.1
            # Mantener informacion estatica
            protocolo_actualizado.nombre = protocolo.nombre
            protocolo_actualizado.codigo = protocolo.codigo
            # Guardar la protocolo
            protocolo_actualizado.save()
            # Cargar mensaje de exito
            messages.add_message(request, messages.SUCCESS, 'El protocolo se ha actualizado correctamente')
            # Retornar a la pagina crearSolicitud
            return HttpResponseRedirect(reverse('actualizarProtocolo'))
        else:
            # Visualizar errores presentados
            print(form_actualizar_protocolo.errors)
    else:
        form_actualizar_protocolo = CrearProtocoloForm()

    # Subir la informacion al contexto
    context = {
        'protocolo': protocolo,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
        'form_actualizar_protocolo': form_actualizar_protocolo,
    }

    return render(request, 'actualizarProtocolo.html', context)
