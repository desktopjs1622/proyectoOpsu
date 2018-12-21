# Librerias Standard
import re

# Librerias Django
from django import forms
from django.forms import (
    CheckboxSelectMultiple, ModelForm, Select, TextInput,
    inlineformset_factory)
from django.utils.safestring import SafeData, SafeText, mark_safe
from django.utils.functional import Promise, keep_lazy, keep_lazy_text
# Librerias de terceros
from dal import autocomplete
from sismeu.models import (
    Clinica, HistoricoClinica, MotivoInactivacion, Region,
    RegionEstado, Departamento, ConvenioClinica, TelefonoClinica, ResponsableRegional)

class ClinicaForm(ModelForm):
    class Meta:
        model = Clinica
        fields = [
            'nombre',
            'rif',
            'estado',
            'municipio',
            'parroquia',
            'direccion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'rif': forms.TextInput(attrs={'class':'form-control'}),
            'estado': autocomplete.ModelSelect2(url='sismeu:EstadoAutoComplete', attrs={'data-placeholder': '-----Estados-----', 'class':'form-control select2'}),
            'municipio': autocomplete.ModelSelect2(url='sismeu:MunicipioAutoComplete', forward=['estado'], attrs={'data-placeholder': '-----Municipios-----', 'class':'form-control select2'}),
            'parroquia': autocomplete.ModelSelect2(url='sismeu:ParroquiaAutoComplete', forward=['municipio'], attrs={'data-placeholder': '-----Parroquias-----', 'class':'form-control select2'}),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
        }

    def clean_rif(self):
        """
        Validamos que el rif cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        rif = diccionario_limpio.get('rif')
        patron = re.compile('^[GgJjVvEe]\-\d{5,8}\-\d{1}$')
        if rif:
            if patron.match(rif) is None:
                raise forms.ValidationError("El número de número de rif debe\
                                            cumplir con la forma J-12345678-9\
                                            , Letras Válidas G-J-V-E.")
        return rif
class ContactoClinicaForm(ModelForm):

    class Meta:
        model = TelefonoClinica
        fields = [
            'departamento',
            'telefono',
            'publicar',
        ]
        widgets = {
            'departamento':forms.Select(attrs={'class':'form-control Select2', 'style':'color:black'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'style':'color:black'}),
        }



def clean_telefono(self):
    """
    Validamos que el teléfono cumpla con el formato
    """
    diccionario_limpio = self.cleaned_data
    telefono = diccionario_limpio.get('telefono')
    patron = re.compile('^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$')
    if telefono:
        if patron.match(telefono) is None:
            raise forms.ValidationError("El número de teléfono local debe\
                                            cumplir con la forma +58 (999)\
                                            999-99-99")
    return telefono

        
class HistoriaForm(ModelForm):
	class Meta:
		model = HistoricoClinica
		fields = (
			'motivo_inactivacion',
			)
		widgets = {
			'motivo_inactivacion':forms.Select(attrs = {'class':'form-control Select2', 'style':'color:black'})
		}

class RegionForm(ModelForm):
    
    class Meta:
        model = Region
        fields = (
            'nombre',
        )
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
        }


class RegionEstadoForm(ModelForm):
	class Meta:
		model = RegionEstado
		exclude = ()

REGIONESTADOFORMSET = inlineformset_factory(
    Region,
    RegionEstado,
    fields=['estado'],
    widgets={'estado':autocomplete.ModelSelect2(url='sismeu:EstadoRegionAutoComplete', attrs={'data-placaholder':'----------Estado----------', 'class':'form-control Select2'})},
    form=RegionEstadoForm,
    extra=1
)

class ResponsableRegionalForm(ModelForm):
    class Meta:
        model = ResponsableRegional
        exclude = ()

RESPONSABLEREGIONALFORMSET = inlineformset_factory(
    Region,
    ResponsableRegional,
    fields=['responsable'],
    widgets={'responsable':forms.Select(attrs={'data-placeholder':'-------Responsable de la Región-------', 'class':'form-control Select2'})},
    form=ResponsableRegionalForm,
    extra=1
)


class MotivoInactivacionForm(ModelForm):
    class Meta:
        model = MotivoInactivacion
        fields = (
            'nombre',
        )



class ConvenioClinicaForm(ModelForm):
	class Meta:
		model = ConvenioClinica
		exclude = ()

CONVENIO_CLINICA_FORMSET = inlineformset_factory(
    Clinica,
    ConvenioClinica,
    fields=['convenio'],
    widgets={
        'convenio':forms.Select(attrs={'class':'form-control Select2'}),
    },
    extra=1
)
