from solicitud.models import Solicitud
from maquina.models import PrestamoMaquina
from django.db import transaction
from django.shortcuts import render
from solicitud.models import TipoSolicitud
from usuario.models import LoginForm, Rol, MenuPorRol
from usuario.models import Usuario
from insumo.models import Insumo
from protocolo.models import ClasificacionProtocolo
from protocolo.models import Protocolo
from experimento.models import Experimento
from proyecto.models import Proyecto
from maquina.models import Maquina
from django.contrib.auth.models import User
import usuario.views as UsuarioView


def index(request):
    inicializarDatos()
    form_login = LoginForm()
    lista_menu = []
    usuario_parametro = ''
    usuario_proyectos = ''
    usuario_experimentos = ''
    usuario_solicitudes = ''
    usuario_maquinas = ''

    if request.user.is_authenticated:
        # Crear el menu del usuario
        lista_menu = UsuarioView.crearMenu(request.user)
        # Cargar el usuario activo
        usuario_parametro = Usuario.objects.get(user_id=request.user.id)

        # Cargar informacion del dashboard
        usuario_proyectos = len(Proyecto.objects.filter(asistentes__user=request.user.id))
        usuario_experimentos = len(Experimento.objects.filter(
            experimento__proyecto_id__in=Proyecto.objects.filter(asistentes__user=request.user.id)))
        usuario_solicitudes = len(Solicitud.objects.filter(usuario_creador=request.user.id))
        usuario_maquinas = len(PrestamoMaquina.objects.filter(usuario=request.user.id))

    context = {'form_login': form_login,
               'lista_menu': lista_menu,
               'usuario_parametro': usuario_parametro,
               'usuario_proyectos': usuario_proyectos,
               'usuario_experimentos': usuario_experimentos,
               'usuario_solicitudes': usuario_solicitudes,
               'usuario_maquinas': usuario_maquinas
               }

    return render(request, 'index.html', context)

def inicializarDatos():
    try:
        with transaction.atomic():
            if (Proyecto.objects.all().count() == 0):
                rol1 = Rol()
                rol1.rol = "rol_cientifico"
                rol1.descripcion = "rol_cientifico"
                rol1.save()

                rol2 = Rol()
                rol2.rol = "rol_asistente"
                rol2.descripcion = "rol_asistente"
                rol2.save()

                rol3 = Rol()
                rol3.rol = "rol_jefe"
                rol3.descripcion = "rol_jefe"
                rol3.save()

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
                usuario1.rol_usuario = rol1
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
                usuario2.rol_usuario = rol2
                usuario2.save()

                user3 = User()
                user3.username = "jefe"
                user3.password = "pbkdf2_sha256$30000$pYq6s9qQGJjg$HKurLl0z+LYBfyW/q4rEClXwapFjx5W5pKwXwGAobdE="
                user3.save()

                usuario3 = Usuario()
                usuario3.user = user3
                usuario3.nombres = "jefe"
                usuario3.apellidos = "jefe"
                usuario3.pais = "jefe"
                usuario3.ciudad = "jefe"
                usuario3.intereses = "jefe"
                usuario3.rol_usuario = rol3
                usuario3.save()

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

                protocolo2 = Protocolo()
                protocolo2.nombre = "protocolo1"
                protocolo2.descripcion = "protocolo1"
                protocolo2.version = 2
                protocolo2.fecha_creacion = "2017-01-01"
                protocolo2.codigo = "1"
                protocolo2.clasificacion = clasificacionProtocolo
                protocolo2.observaciones = "protocolo1"
                protocolo2.save()
                protocolo2.insumos.add(insumo1)
                protocolo2.insumos.add(insumo2)
                protocolo2.save()

                experimento1 = Experimento()
                experimento1.nombre = "experimento1"
                experimento1.descripcion = "experimento1"
                experimento1.estado = "experimento1"
                experimento1.fecha_resultado = "2017-01-01"
                experimento1.save()
                experimento1.protocolos.add(protocolo1)
                experimento1.save()

                proyecto1 = Proyecto()
                proyecto1.nombre = "Proyecto Umbrella"
                proyecto1.descripcion = "Proyecto para creacion de armas quimicas"
                proyecto1.estado = 'Activo'
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

                menuCientifico1 = MenuPorRol()
                menuCientifico1.menu = "Proyectos"
                menuCientifico1.opcion = "Ver Proyectos"
                menuCientifico1.template = "../proyectos"
                menuCientifico1.rol = rol1
                menuCientifico1.save()

                menuCientifico2 = MenuPorRol()
                menuCientifico2.menu = "Experimentos"
                menuCientifico2.opcion = "Ver Experimentos"
                menuCientifico2.template = "../proyectos"
                menuCientifico2.rol = rol1
                menuCientifico2.save()

                menuCientifico3 = MenuPorRol()
                menuCientifico3.menu = "Protocolos"
                menuCientifico3.opcion = "Buscar Protocolo"
                menuCientifico3.template = "../buscarProtocolo"
                menuCientifico3.rol = rol1
                menuCientifico3.save()

                menuCientifico4 = MenuPorRol()
                menuCientifico4.menu = "Ordenes"
                menuCientifico4.opcion = "Listar Ordenes"
                menuCientifico4.template = "../ordenes"
                menuCientifico4.rol = rol1
                menuCientifico4.save()

                menuCientifico5 = MenuPorRol()
                menuCientifico5.menu = "Solicitudes"
                menuCientifico5.opcion = "Gestionar Solicitudes"
                menuCientifico5.template = "../menuSolicitud"
                menuCientifico5.rol = rol1
                menuCientifico5.save()

                menuAsistente1 = MenuPorRol()
                menuAsistente1.menu = "Proyectos"
                menuAsistente1.opcion = "Ver Proyectos"
                menuAsistente1.template = "../proyectos"
                menuAsistente1.rol = rol2
                menuAsistente1.save()

                menuAsistente2 = MenuPorRol()
                menuAsistente2.menu = "Experimentos"
                menuAsistente2.opcion = "Ver Experimentos"
                menuAsistente2.template = "../proyectos"
                menuAsistente2.rol = rol2
                menuAsistente2.save()

                menuAsistente3 = MenuPorRol()
                menuAsistente3.menu = "Protocolos"
                menuAsistente3.opcion = "Buscar Protocolo"
                menuAsistente3.template = "../buscarProtocolo"
                menuAsistente3.rol = rol2
                menuAsistente3.save()

                menuAsistente4 = MenuPorRol()
                menuAsistente4.menu = "Ordenes"
                menuAsistente4.opcion = "Listar Ordenes"
                menuAsistente4.template = "../ordenes"
                menuAsistente4.rol = rol2
                menuAsistente4.save()

                menuAsistente5 = MenuPorRol()
                menuAsistente5.menu = "Solicitudes"
                menuAsistente5.opcion = "Gestionar Solicitudes"
                menuAsistente5.template = "../menuSolicitud"
                menuAsistente5.rol = rol2
                menuAsistente5.save()

                menuJefe1 = MenuPorRol()
                menuJefe1.menu = "Proyectos"
                menuJefe1.opcion = "Ver Proyectos"
                menuJefe1.template = "../proyectos"
                menuJefe1.rol = rol3
                menuJefe1.save()

                menuJefe2 = MenuPorRol()
                menuJefe2.menu = "Experimentos"
                menuJefe2.opcion = "Ver Experimentos"
                menuJefe2.template = "../proyectos"
                menuJefe2.rol = rol3
                menuJefe2.save()

                menuJefe3 = MenuPorRol()
                menuJefe3.menu = "Solicitudes"
                menuJefe3.opcion = "Gestionar Solicitudes"
                menuJefe3.template = "../menuSolicitud"
                menuJefe3.rol = rol3
                menuJefe3.save()

    except:
        pass