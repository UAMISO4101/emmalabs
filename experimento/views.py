# coding=utf-8
from django.shortcuts import render
import usuario.views as UsuarioView
from django.http import HttpResponseRedirect
from django.contrib import messages
from experimento.forms import ExperimentoForm
from experimento.models import Experimento
from proyecto.models import Proyecto
from usuario.models import Usuario
from django.urls import reverse


def crear_experimento(request, id):
    # Crear el menu del usuario
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = ExperimentoForm(request.POST)
        # Validar formulario
        if form.is_valid():
            experimento = form.save()
            # Guardar la solicitud
            experimento.save()

            proyecto = Proyecto.objects.get(id=id)
            proyecto.experimentos.add(experimento)
            proyecto.save()

            # Cargar mensaje de exito
            messages.add_message(request, messages.SUCCESS, 'El experimento se ha creado correctamente')
            # Retornar a la pagina crearSolicitud

            return HttpResponseRedirect(reverse('proyectos', args=(id)))
        else:
            # Visualizar errores presentados
            print(form.errors)
    else:
        form = ExperimentoForm()

    context = {
        'form': form,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
    }

    return render(request, 'crearExperimento.html', context)


def detalleProyecto(request, id):
    # Inicializar variables
    lista_menu = UsuarioView.crearMenu(request.user)
    # Cargar el usuario activo
    usuario_parametro = Usuario.objects.get(user_id=request.user.id)
    print ('Usuario_parametro')
    print ('rol_usuario=', usuario_parametro.rol_usuario.rol)

    if (request.method == "POST"):
        resultado = request.POST['resultado']
        id = request.POST['experimento_id']
        experimento = Experimento.objects.get(id=id)
        experimento.resultado = resultado
        experimento.save()

    proyecto = Proyecto.objects.get(id=id)

    context = {
        'proyecto': proyecto,
        'lista_menu': lista_menu,
        'usuario_parametro': usuario_parametro,
    }
    return render(request, 'detalle_proyecto.html', context)
