# -*- coding: utf-8 -*-
from django.shortcuts import render

from .forms import ProtocoloForm


def buscar_protocolo_vista(request):
    # Inicializa el formulario
    protocolo_form = ProtocoloForm()
    if request.method == 'POST':
        # Envia el formulario con los datos diligenciados por el usuario
        protocolo_form = ProtocoloForm(data=request.POST)
        # Validar si el formulario es correcto
        if protocolo_form.is_valid():
            # guardar el protocolo
            pass

    context = {
        'formProtocolo': protocolo_form,
    }

    return render(request, 'buscarProtocolos.html', context)
