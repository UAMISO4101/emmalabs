from django.shortcuts import render

from .forms import ProtocoloForm


def buscar_protocolo_vista(request):
    # Inicializa el formulario
    protocolo_form = ProtocoloForm(data=request.POST)
    if request.method == 'POST':
        # Validar si el formulario es correcto
        if protocolo_form.is_valid():
            # guardar el protocolo
            pass

    context = {
        'formProtocolo': protocolo_form,
    }

    return render(request, 'buscarProtocolos.html', context)
