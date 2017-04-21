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
            'cientifico',
        ]
        labels = {
            'titulo' : 'Titulo',
            'tipo' : 'Tipo de solicitud',
            'texto' : 'Mensaje',
            'cientifico' : 'Dirigido al cientifico',
        }
        widgets = {
            'texto': forms.Textarea,
        }