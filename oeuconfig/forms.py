# -*- coding: utf-8 -*-
"""
Formularios de aplicación OEUConfig
"""
# Librerias Standard
import datetime

# Librerias Django
from django import forms
from django.forms import ModelForm

# Librerias de terceros
from oeuconfig.models import SoporteFormalCambio


##############################################################################
class SfcForm(ModelForm):
    """
    Formulario ajustado para manipular los soportes formales de cambio
    """
    class Meta:
        model = SoporteFormalCambio
        fields = (
            'tipo_sfc',
            'nombre',
            'numero',
            'numero_gaceta',
            'fecha_gaceta',
            'archivo_adjunto'
        )
        widgets = {
            'tipo_sfc': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'minlength': '4',
                'maxlength': '10'}),
            'numero_gaceta': forms.TextInput(attrs={
                'class': 'form-control',
                'minlength': '4',
                'maxlength': '10'}),
            'fecha_gaceta': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        diccionario_limpio = self.cleaned_data
        fecha_gaceta = diccionario_limpio.get('fecha_gaceta')
        
        #Validamos que la gaceta tiene fecha inferior al horario del servidor
        fecha_actual = datetime.date.today()
        fecha = fecha_actual.day - fecha_gaceta.day - ((fecha_actual.year, fecha_actual.month) < (fecha_gaceta.year, fecha_gaceta.month))
        if fecha < 1:
            self.add_error('fecha_gaceta', "Disculpe, debe corregir la fecha seleccionada")
