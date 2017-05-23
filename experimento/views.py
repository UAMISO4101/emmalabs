# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from experimento.forms import ExperimentoForm
from experimento.models import Experimento
from proyecto.models import Proyecto
from usuario.models import Usuario
from django.urls import reverse


def crear_experimento(request):
    if request.method == 'POST':
        form = ExperimentoForm(request.POST)
        # Validar formulario
        if form.is_valid():
            proyecto = form.save(commit=False)
            # Se debe guardar el usuario creador
            proyecto.cientifico_asignado = Usuario.objects.get(user=request.user)
            # Guardar la solicitud
            proyecto.save()
            # Cargar mensaje de exito
            messages.add_message(request, messages.SUCCESS, 'El experimento se ha creado correctamente')
            # Retornar a la pagina crearSolicitud
            return HttpResponseRedirect(reverse('crearExperimento'))
        else:
            # Visualizar errores presentados
            print(form.errors)
    else:
        form = ExperimentoForm()

    return render(request, 'crearExperimento.html', {'form':form})

def detalleProyecto(request, id):
    if(request.method == "POST"):
        resultado = request.POST['resultado']
        id = request.POST['experimento_id']
        experimento = Experimento.objects.get(id=id)
        experimento.resultado = resultado
        experimento.save()
    proyecto = Proyecto.objects.get(id=id)
    context = {
        'proyecto': proyecto
    }
    return render(request, 'detalle_proyecto.html', context)