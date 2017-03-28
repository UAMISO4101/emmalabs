# coding=utf-8
from django.shortcuts import render

# Create your views here.
from .models import Proyecto


def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    context = {'lista_proyectos': lista_proyectos}
    return render(request, 'proyectos.html', context)

def detalleProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    context = {
        'proyecto': proyecto
    }
    return render(request, 'detalle_proyecto.html', context)