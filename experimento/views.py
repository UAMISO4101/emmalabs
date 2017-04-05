# coding=utf-8
from django.shortcuts import render
from experimento.models import Experimento
from proyecto.models import Proyecto


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


def prueba_plantilla(request):
    return render(request, 'prueba_plantilla.html')