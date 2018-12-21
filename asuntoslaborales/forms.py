# -*- coding: utf-8 -*-
# Django Library
# Django Library
# Django Library
# Django Library
# Django Library
# Django Library
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
# Librerias Django
from django.contrib import messages
from django.forms import (
    CheckboxInput, CheckboxSelectMultiple, HiddenInput, ModelForm, Select,
    TextInput)

# Librerias de terceros
# Thirdparty Library
from asuntoslaborales.models import HistoriaLaboral
from dal import autocomplete
from suit.widgets import SuitDateWidget


#####################################################################################################################################
########################################### Formulario customizado de la Historia Laboral ###########################################
class HistoriaLaboralForm(ModelForm):
    class Meta:
        model = HistoriaLaboral
        fields = (
            'persona',
            'institucion',
            'tipo_personal',
            'fecha_ingreso',
            'fecha_egreso',
            'condicion_egreso',
        )
        widgets = {
            'persona': autocomplete.ModelSelect2(url='globales:personaAutoComplete', forward=['sexo'], attrs={'data-placeholder': '----------', 'data-minimum-input-length': 3, 'class': 'form-control input-sm'}),
            'institucion': autocomplete.ModelSelect2(url='oeu:institucion-ieu', attrs={'data-placeholder': 'Institución de Educación Universitaria ...',},),
            'tipo_personal': Select(attrs={'class':'form-control input-sm'}),
            'fecha_ingreso': SuitDateWidget(),
            'fecha_egreso': SuitDateWidget(),
            'condicion_egreso': Select(attrs={'class':'form-control input-sm'}),
        }
