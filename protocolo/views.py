# -*- coding: utf-8 -*-
from django.shortcuts import render

from .forms import ProtocoloForm
from .models import Protocolo


def buscar_protocolo_vista(request):
    # Inicializa listado de protocolos
    lista_protocolos = Protocolo.objects.all()

    if request.method == 'POST':
        # Envia el formulario con los datos diligenciados por el usuario
        protocolo_form = ProtocoloForm(data=request.POST)
        # Validar si el formulario es correcto
        if protocolo_form.is_valid():
            # Validar que criterio de busqueda se va a aplicar
            lista_protocolos = Protocolo.objects.filter(nombre__contains=request.POST.get('nombre_protocolo'))
    else:
        # Inicializa formulario vacio
        protocolo_form = ProtocoloForm()

    context = {
        'formProtocolo': protocolo_form,
        'lista_protocolos': lista_protocolos
    }

    return render(request, 'buscarProtocolos.html', context)
