from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'data-mask': "00/00/0000", 'placeholder': 'mes/día/año'}),
        }

        error_messages = {
            'fecha_nacimiento': {
                'invalid': 'Por favor, ingresa una fecha válida en el formato mes/día/año.',
            },
        } 