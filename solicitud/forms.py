from django import forms

from solicitud.models import Solicitud

# Formulario de una solicitud
class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'titulo',
            'tipo',
            'texto',
            'usuario_destino',
        ]
        labels = {
            'titulo' : 'Titulo',
            'tipo' : 'Tipo de solicitud',
            'texto' : 'Mensaje',
            'usuario_destino' : 'Dirigido a',
        }
        widgets = {
            'texto': forms.Textarea,
        }