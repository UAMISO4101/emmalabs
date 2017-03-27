from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudForm

# Vista para crear una solicitud
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            # Guardar la solicitud
            form.save()
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