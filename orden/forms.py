from django import forms

from orden.models import Orden

# Formulario de una solicitud
class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden

        fields = [
            'nombre',
            'descripcion',
        ]
        labels = {
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
        }
        widgets = {
            'descripcion': forms.Textarea,
        }