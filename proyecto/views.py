# coding=utf-8
from django.shortcuts import render
from .models import Proyecto

def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    context = {'lista_proyectos': lista_proyectos}
    return render(request, 'proyectos.html', context)