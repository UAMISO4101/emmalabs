from django.db import transaction
from django.shortcuts import render

from solicitud.models import TipoSolicitud
from usuario.models import LoginForm
from proyecto.models import Proyecto
from usuario.models import Usuario
from insumo.models import Insumo
from protocolo.models import ClasificacionProtocolo
from protocolo.models import Protocolo
from experimento.models import Experimento
from proyecto.models import Proyecto
from maquina.models import Maquina
from django.contrib.auth.models import User

def index(request):
    form_login = LoginForm()
    context = {'form_login': form_login, }
    inicializarDatos()
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')

def inicializarDatos():
	try:
		with transaction.atomic():
		    if (Proyecto.objects.all().count() == 0):
			user1 = User()
			user1.username = "cientifico"
			user1.password = "pbkdf2_sha256$30000$pYq6s9qQGJjg$HKurLl0z+LYBfyW/q4rEClXwapFjx5W5pKwXwGAobdE="
			user1.save()

			usuario1 = Usuario()
			usuario1.user = user1
			usuario1.nombres = "cientifico"
			usuario1.apellidos = "cientifico"
			usuario1.pais = "cientifico"
			usuario1.ciudad = "cientifico"
			usuario1.intereses = "cientifico"
			usuario1.rol = "cientifico"
			usuario1.save()

			user2 = User()
			user2.username = "asistente"
			user2.password = "pbkdf2_sha256$30000$pYq6s9qQGJjg$HKurLl0z+LYBfyW/q4rEClXwapFjx5W5pKwXwGAobdE="
			user2.save()

			usuario2 = Usuario()
			usuario2.user = user2
			usuario2.nombres = "asistente"
			usuario2.apellidos = "asistente"
			usuario2.pais = "asistente"
			usuario2.ciudad = "asistente"
			usuario2.intereses = "asistente"
			usuario2.rol = "asistente"
			usuario2.save()

			insumo1 = Insumo()
			insumo1.nombre = "insumo1"
			insumo1.descripcion = "insumo1"
			insumo1.cantidad = 1
			insumo1.unidades = "Unidades"
			insumo1.save()

			insumo2 = Insumo()
			insumo2.nombre = "insumo2"
			insumo2.descripcion = "insumo2"
			insumo2.cantidad = 1
			insumo2.unidades = "Unidades"
			insumo2.save()

			clasificacionProtocolo = ClasificacionProtocolo()
			clasificacionProtocolo.nombre_clasificacion = "Sin clasificacion"
			clasificacionProtocolo.save()

			protocolo1 = Protocolo()
			protocolo1.nombre = "protocolo1"
			protocolo1.descripcion = "protocolo1"
			protocolo1.version = 1
			protocolo1.fecha_creacion = "2017-01-01"
			protocolo1.codigo = "1"
			protocolo1.clasificacion = clasificacionProtocolo
			protocolo1.observaciones = "protocolo1"
			protocolo1.save()
			protocolo1.insumos.add(insumo1)
			protocolo1.insumos.add(insumo2)
			protocolo1.save()

			experimento1 = Experimento()
			experimento1.nombre = "experimento1"
			experimento1.descripcion = "experimento1"
			experimento1.estado = "experimento1"
			experimento1.resultado = "experimento1"
			experimento1.fecha_resultado = "2017-01-01"
			experimento1.save()
			experimento1.protocolos.add(protocolo1)
			experimento1.save()

			proyecto1 = Proyecto()
			proyecto1.nombre = "proyecto1"
			proyecto1.descripcion = "proyecto1"
			proyecto1.estado = "proyecto1"
			proyecto1.fecha_creacion = "2017-01-01"
			proyecto1.cientifico_asignado = usuario1
			proyecto1.save()
			proyecto1.experimentos.add(experimento1)
			proyecto1.asistentes.add(usuario2)
			proyecto1.save()

			maquina1 = Maquina()
			maquina1.nombre = "maquina1"
			maquina1.descripcion = "maquina1"
			maquina1.save()

			maquina2 = Maquina()
			maquina2.nombre = "maquina2"
			maquina2.descripcion = "maquina2"
			maquina2.save()

			tipoSolicitud = TipoSolicitud()
			tipoSolicitud.nombre = "Compra"
			tipoSolicitud.save()
	except SomeError:
		handle_exception()