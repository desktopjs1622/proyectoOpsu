# Librerias Django
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

# Librerias de terceros
from dal import autocomplete

# Librerias desarrolladas por mi
from oeu.models import Carrera, SubAreaConocimiento, CarreraSfc


class SubAreaConocimientoForm(ModelForm):
    """
    Formulario ajustado para manipular las sub áreas de conocimientos
    """
    class Meta:
        """
        Describo mi modelos, los campos y sus atributos
        """
        model = SubAreaConocimiento

        fields = [
            'id_area_conocimiento',
            'nombre_subarea_conocimiento'
        ]

        widgets = {
            'id_area_conocimiento': forms.Select(attrs={'class':'form-control'}),
            'nombre_subarea_conocimiento': forms.TextInput(attrs = {
                'class':'form-control', 
                'placeholder':'Escribe la sub área de conocimiento asociada'
            }),
        }

##############################################################################

class CarreraPreGradoForm(ModelForm):
    """
    Formulario ajustado para manipular las carreras de pre grado
    """
    class Meta:
        model = Carrera

        fields = [
            'localidad_edit',
            'nombre_edit',
            'descripcion_edit',
            'titulo_edit',
            'tipo_carrera_edit',
            'ieu_acreditadora_edit',
            'mercado_ocupacional_edit',
            'area_conocimiento_edit',
            'sub_area_conocimiento_edit',
            'cine_f_campo_amplio_edit',
            'cine_f_campo_especifico_edit',
            'cine_f_campo_detallado_edit',
            'duracion_edit',
            'modalidad_edit',
            'prioritaria_edit',
            'cod_activacion',
            'publicar'
        ]

        labels = {
            'localidad_edit': ('Localidad'),
            'nombre_edit': ('Nombre'),
            'descripcion_edit': ('Descripción'),
            'titulo_edit': ('Título'),
            'tipo_carrera_edit':('Tipo de Carrera'),
            'ieu_acreditadora_edit': ('Institución Acreditadora'),
            'mercado_ocupacional_edit': ('Mercado Ocupacional'),
            'area_conocimiento_edit': ('Área de Conocimiento'),
            'sub_area_conocimiento_edit': ('Sub Área de Conocimiento'),
            'cine_f_campo_amplio_edit': ('Campo Amplio'),
            'cine_f_campo_especifico_edit': ('Campo Especifico'),
            'cine_f_campo_detallado_edit': ('Campo Detallado'),
            'duracion_edit': ('Duración'),
            'modalidad_edit': ('Modalidad'),
        }

        widgets = {
            'localidad_edit':autocomplete.ModelSelect2(
                url='oeuacademic:localidades',
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Selecciona la Localidad'
                    },
                ),
            'nombre_edit':forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder':'Escribe el nombre de la Carrera'
                    },
                ),
            'descripcion_edit':forms.Textarea(
                attrs={
                    'class':'form-control', 
                    'placeholder':'Haz una descripción de la Carrera', 
                    'rows':2},
                ),
            'titulo_edit':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Título'},),
            'tipo_carrera_edit':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Seleccione Una Opción'},),
            'ieu_acreditadora_edit':autocomplete.ModelSelect2(
                url='oeuacademic:acreditadora',
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Institución Acreditadora'
                    },
                ),
            'mercado_ocupacional_edit':forms.Textarea(
                attrs={
                    'class':'form-control', 
                    'placeholder':'Escribe el mercado ocupacional de la carrera', 
                    'rows':2},
                ),
            'area_conocimiento_edit':autocomplete.ModelSelect2(
                url='oeuacademic:area-conocimiento',
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Área de Conocimiento'
                    },
                ),
            'sub_area_conocimiento_edit':autocomplete.ModelSelect2(
                url='oeuacademic:sub-area-conocimiento',
                forward=['area_conocimiento_edit'],
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Sub Área de Conocimiento'
                    },
                ),
            'cine_f_campo_amplio_edit':autocomplete.ModelSelect2(
                url='oeuacademic:cine-f-campo-amplio',
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Seleccione Una Opción'
                    },
                ),
            'cine_f_campo_especifico_edit':autocomplete.ModelSelect2(
                url='oeuacademic:cine-f-campo-especifico',
                forward=['cine_f_campo_amplio_edit'],
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Seleccione Una Opción'
                    },
                ),
            'cine_f_campo_detallado_edit':autocomplete.ModelSelect2(
                url='oeuacademic:cine-f-campo-detallado',
                forward=['cine_f_campo_especifico_edit'],
                attrs={
                    'class':'form-control select2',
                    'data-placeholder':'Seleccione Una Opción'
                    },
                ),
            'duracion_edit':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Duración de la Carrera'},),
            'modalidad_edit':forms.Select(attrs={'class':'form-control'},),
            'prioritaria_edit':forms.RadioSelect(),
            
        }

##############################################################################
class CarreraSfcForm(ModelForm):
    class Meta:
        model = CarreraSfc
        exclude = ()


CARRERA_FORMSET = inlineformset_factory(
    Carrera,
    CarreraSfc,
    fields=['sfc'],
    widgets={'sfc': forms.Select(attrs={'class':'form-control'})},
    form=CarreraSfcForm,
    extra=1
    )