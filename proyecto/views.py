# coding=utf-8
from django.shortcuts import render

# Create your views here.
from experimento.models import Experimento
from .models import Proyecto


def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    context = {'lista_proyectos': lista_proyectos}
    return render(request, 'proyectos.html', context)

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