from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from usuario.models import Usuario
from .forms import SolicitudForm
from .models import Solicitud

# Vista para crear una solicitud
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        # Validar formulario
        if form.is_valid():
            solicitud = form.save(commit=False)
            # Se debe guardar el usuario creador
            solicitud.asistente = Usuario.objects.get(user=request.user)
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

    return render(request, 'crearSolicitud.html', {'form':form})


def menu_solicitud(request):
    return render (request, 'menuSolicitud.html')

# Vista para listar las solicitudes del usuario
def listar_solicitudes(request):
    usuario = Usuario.objects.get(user = request.user)
    # Se filtran las solicitudes por usuario creador
    lista_solicitudes = Solicitud.objects.filter(asistente=usuario).order_by('-fecha_creacion')

    context = {'lista_solicitudes': lista_solicitudes}
    return render(request, 'solicitudes.html', context)