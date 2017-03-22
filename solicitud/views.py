from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SolicitudForm

# Create your views here.
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('solicitud:crearSolicitud')
        return HttpResponseRedirect(reverse('crearSolicitud'))
    else:
        form = SolicitudForm()

    return render(request, 'crearSolicitud.html', {'form':form})