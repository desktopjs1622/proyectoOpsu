from django import forms
from django.forms import Select, SelectMultiple
from .models import SeguidorEstadal
from django.db.models import Q
from dal import autocomplete
from cuenta.models import Persona

class SeguidorEstadalForm(forms.ModelForm):
    class Meta:
        model = SeguidorEstadal
        fields = [
            'persona',
            'estado',
        ]
        labels = {
            'persona': 'Seguidor',
            'estado': 'Estado',
        }
        widgets = {
            'persona': Select(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione una persona ...',
                },
            ),
            'estado':forms.SelectMultiple(attrs={'class':'form-control', 
                    'data-placeholder': 'Seleccione los estados ...', 'multiple':'multiple'}),
        }

    def __init__(self, *args, **kwargs):
        super(SeguidorEstadalForm, self).__init__(*args, **kwargs)
        seguidores = SeguidorEstadal.objects.all().values('persona')
        self.fields['persona'].queryset = Persona.objects.filter(~Q(pk__in=seguidores))