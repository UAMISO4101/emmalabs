# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render

from .forms import ProtocoloForm
from .models import Protocolo, Paso, ComentarioProtocolo, Usuario


def buscar_protocolo_vista(request):
    # Inicializa listado de protocolos
    lista_protocolos = Protocolo.objects.all()
    # Bandera para mostrar/ocultar los resultados
    mostrar_resultados = False

    if request.method == 'POST':
        # Envia el formulario con los datos diligenciados por el usuario
        protocolo_form = ProtocoloForm(data=request.POST)
        # Validar si el formulario es correcto
        if protocolo_form.is_valid():
            mostrar_resultados = True
            # Aplicar criterios de busqueda

            # Si el usuario digita el codigo unico del protocolo se busca directo
            if len(request.POST.get('codigo')) > 0:
                lista_protocolos = Protocolo.objects.filter(codigo__contains=request.POST.get('codigo'))
            elif request.POST.get('fecha_creacion') != '':
                # Se requiere que la fecha coincida con el formato de la base de datos
                fecha_sin_formato = request.POST.get('fecha_creacion')
                fecha_con_formato = datetime.datetime.strptime(fecha_sin_formato, '%m/%d/%Y').strftime('%Y-%m-%d')
                lista_protocolos = Protocolo.objects.filter(fecha_creacion=fecha_con_formato)
            elif request.POST.get('clasificacion') is not None:
                lista_protocolos = Protocolo.objects.filter(
                    clasificacion__nombre_clasificacion__contains=request.POST.get('clasificacion'))
            else:
                lista_protocolos = Protocolo.objects.filter(nombre__contains=request.POST.get('nombre'))

    else:  # Si el request es de tipo get
        # Inicializa formulario vacio
        protocolo_form = ProtocoloForm()

    context = {
        'formProtocolo': protocolo_form,
        'lista_protocolos': lista_protocolos,
        'mostrar_resultados': mostrar_resultados,
    }

    return render(request, 'buscarProtocolos.html', context)


def detalle_protocolo_vista(request, id_protocolo):
    if(request.method == "POST"):
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
    comentarios_protocolo = ComentarioProtocolo.objects.filter(protocolo=id_protocolo).order_by('id')

    # Subir la informacion al contexto
    context = {
        'protocolo': protocolo,
        'lista_pasos': lista_pasos,
        'lista_insumos': lista_insumos,
        'comentarios_protocolo': comentarios_protocolo
    }
    return render(request, 'protocolos.html', context)
