# -*- coding: utf-8 -*-
"""
Formularios para la app globales
"""
# Librerias Django
from django import forms

# Librerias de terceros
from dal import autocomplete

# Librerias desarrolladas por mi
from oeu.models import Ieu, Localidad

# Librerias en carpetas locales
from .models import Actogrado, Graduando, LocalidadPersona

# from django_select2.forms import (
#     HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
#     ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
#     Select2Widget
# )


class ActogradoForm(forms.ModelForm):
    """
    Formulario ajustado para manipular los tipos de institución de la oferta académica
    """
    class Meta:
        model = Actogrado
        fields = (
            'fecha_acto',
            
        )

    # def clean_fecha_acto(self):
    #     fecha = self.cleaned_data['fecha_acto']
    #     if fecha.day < timezone.now().day:
    #         raise forms.ValidationError("Usted esta intentando aperturar un acto en una fecha anterior al día de hoy!")
    #     return fecha


    # def clean(self):
    #     diccionario_limpio = self.cleaned_data
    #     fecha_acto = diccionario_limpio.get('fecha_acto')

    #     #Validamos que los actos de grado sean pautados para la fecha presente o futuras, nunca anteriores.
    #     fecha_actual = datetime.date.today()
    #     if fecha_acto.day < fecha_actual.day:
    #         self.add_error('Los Actos Académicos de Grado, no se pueden pautar para fechas anteriores al día de hoy.')


###############################################################################

class GraduandoForm(forms.ModelForm):
    # cod_institucion = forms.ModelChoiceField(
    #     queryset=Institucion.objects.all(),
    #     widget=autocomplete.ModelSelect2(
    #         url='oeu:institucion-ieu',
    #         attrs={'data-placeholder': 'Institución de Educación Universitaria ...','class': 'form-control col-md-7 col-xs-12 input-sm'},
    #     ),
        
    # )
    # localidad = forms.ModelChoiceField(
    #     queryset=Localidad.objects.all(),
    #     widget=autocomplete.ModelSelect2(
    #         url='oeu:localidad-ieu',
    #         forward=['cod_institucion'],
    #         attrs={'data-placeholder': 'Institución de Educación Universitaria ...','class': 'form-control col-md-7 col-xs-12 input-sm'},
    #     ),
        
    # )
 
    class Meta:
        model = Graduando
        fields = (
            # 'actogrado_id',
            'carrera',
            'persona',

        )
        widgets = {
            # 'actogrado_id': autocomplete.ModelSelect2(url='grado:NumActogradoAutocomplete', forward=['localidad'], attrs={'data-placeholder': 'Nro de Acto de Grado ...', 'class':'input-field form-control col-md-7 col-xs-12 input-sm'},),
            'carrera': autocomplete.ModelSelect2(url='oeu:carrera', forward=['localidad'], attrs={'data-placeholder': 'Carrera ...', 'class':'form-control'},),
            'persona': autocomplete.ModelSelect2(url='globales:personaAutoComplete', attrs={'data-placeholder': 'Persona ...', 'class':'form-control'},),

        }


###############################################################################


class LocalidadPersonaForm(forms.ModelForm):
   
    class Meta:
        model = LocalidadPersona

        fields = [
            'persona',
            'localidad',            
        ]

        widgets = {
            'persona': autocomplete.ModelSelect2(url='globales:personaAutoComplete', attrs={'data-placeholder': 'Persona ...', 'class':'input-field'},),
            'localidad': autocomplete.ModelSelect2(url='oeu:localidad-ieu', forward=['persona_id'] ,attrs={'data-placeholder': 'IEU - Sede ...', 'class':'input-field'},),            
        }

#################################################################################
