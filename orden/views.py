from django.shortcuts import render

# Create your views here.
from .models import Orden


def ordenes(request):
    lista_ordenes = Orden.objects.all()
    context = {'lista_ordenes': lista_ordenes}
    return render(request, 'ordenes.html', context)