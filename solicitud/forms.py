from django import forms

from solicitud.models import Solicitud

# Formulario de una solicitud
class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'titulo',
            'texto',
            'usuario_creador',
            'usuario_destino',
        ]
        labels = {
            'titulo' : 'Titulo',
            'texto' : 'Texto',
            'usuario_creador' : 'Asistente',
            'usuario_destino' : 'Cientifico',
        }
        widgets = {
            'texto': forms.Textarea,
        }