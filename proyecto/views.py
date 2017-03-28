# coding=utf-8
from django.shortcuts import render

# Create your views here.
from .models import Proyecto


def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    context = {'lista_proyectos': [
        {'nombre':"mi nombre 002", 'descripcion':"desc 001", "estado":"Activo", "fecha_de_creacion": "08/02/2017"},
        {'nombre':"mi nombre 003", 'descripcion':"desc 002", "estado":"Terminado", "fecha_de_creacion": "25/01/2017"},
        {'nombre':"mi nombre 004", 'descripcion':"desc 003", "estado":"Cancelado", "fecha_de_creacion": "07/02/2016"},
        {'nombre':"mi nombre 005", 'descripcion':"desc 004", "estado":"Activo", "fecha_de_creacion": "03/06/2014"},
        {'nombre':"mi nombre 006", 'descripcion':"desc 005", "estado":"Activo", "fecha_de_creacion": "18/09/2016"},
        {'nombre':"mi nombre 007", 'descripcion':"desc 006", "estado":"Activo", "fecha_de_creacion": "026/03/2015"}
    ]}

    #context = {'lista_proyectos': lista_proyectos}
    return render(request, 'proyectos.html', context)

def detalleProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    context = {
        'proyecto': proyecto
    }
    return render(request, 'detalle_proyecto.html', context)