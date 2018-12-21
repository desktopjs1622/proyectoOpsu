# -*- coding: utf-8 -*-
"""
Formularios de aplicación OEU
"""
# Librerias Django
from django import forms
from django.contrib import messages
from django.forms import ModelForm, widgets
from django.forms.models import inlineformset_factory
from django.utils.safestring import mark_safe

# Librerias de terceros
from dal import autocomplete
from leaflet.forms.widgets import LeafletWidget

# Librerias desarrolladas por mi
from oeu.models import (
    Ieu, IeuSfc, Localidad, LocalidadSfc, SubTipoInstitucion,
    SubTipoInstitucionSfc, TipoEspecificoIeuSfc, TipoEspecificoInstitucion,
    TipoInstitucion, TipoInstitucionSfc)


##############################################################################
def valida_editor(self, editor):
    """
    Esta función valida si el usuario editor no existe previamente lo agrego
    """
    if editor and (self.request.user.username not in editor):
        return editor + ', ' + self.request.user.username
    elif editor and (self.request.user.username in editor):
        return editor
    else:
        return self.request.user.username


##############################################################################
class TipoInstitucionForm(ModelForm):
    """
    Formulario ajustado para manipular los tipos de institución de la oferta
    académica
    """
    nombre_tipo = forms.CharField(disabled=True, label='Nombre Tipo IEU', required=False)
    orden = forms.CharField(disabled=True, label='Orden IEU', required=False)
    usuario_revisor = forms.CharField(disabled=True, label='Revisor(es)', required=False)
    usuario_editor = forms.CharField(disabled=True, label='Editor', required=False)
    revisor_edit = forms.CharField(disabled=True, label='')
    cod_activacion = forms.ChoiceField(widget=forms.RadioSelect(), label='Activo/Inactivo')

    class Meta:
        model = TipoInstitucion
        fields = (
            'cod_activacion',
        )
        labels = {
            'nombre_edit': (''),
            'orden_edit': (''),
            'revisor_edit': ('')
        }

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        super(TipoInstitucionForm, self).__init__(*args, **kwargs)

        # self.fields['revisor_edit'].widget.attrs['readonly'] = True

        # Concateno a los revisores
        # self.initial['revisor_edit'] = 'a' #valida_editor(self, self.instance.revisor_edit)

        # Si estoy editando un registro incializo los campos
        if self.instance.pk:
            self.initial['nombre_tipo'] = self.instance.nombre
            self.initial['orden'] = self.instance.orden
            self.initial['usuario_revisor'] = self.instance.revisor
            self.initial['usuario_editor'] = self.instance.editor
            current_cod_activacion = self.instance.cod_activacion

            # Construyo su codigo de validadción de acuerdo al modelo (tabla) correspondiente
            # tratarse del modelo TipoInstitucion debemos controlar el bit 8 (posición 7 en la
            # lista) del cod_activacion.

            # Al guardar siempre se debe inactivar el bit de revisado (bit 2 posicion 1 en la lista)
            # para indicar que este registro fue revisado por alguien
            current_cod_activacion = list(current_cod_activacion)
            current_cod_activacion[1] ='0'
            current_cod_activacion = ''.join(current_cod_activacion)

            if current_cod_activacion[7:8] == '1':
                activo = current_cod_activacion
                inactivo = list(activo)
                inactivo[7] = '0'
                inactivo = ''.join(inactivo)
            else:
                inactivo = list(current_cod_activacion)
                activo = list(inactivo)
                activo[7] = '1'
                activo = ''.join(activo)
        else:
            activo = '00000001'
            inactivo = '00000000'
            current_cod_activacion = activo

        CODACTIVACION = (
            (activo, 'Activo'),
            (inactivo, 'Inactivo')
        )

        self.fields['cod_activacion'].choices = CODACTIVACION
        self.initial['cod_activacion'] = current_cod_activacion

        # Preparar mensaje de inactivación:
        if current_cod_activacion != '01000001' and current_cod_activacion != '11000001' and current_cod_activacion != '10000001' and current_cod_activacion != '00000001' and self.instance.pk:
            mensaje = mark_safe('Este tipo de IEU se encuentra inactivo:')
            if current_cod_activacion[7:8] == '0':
                mensaje += mark_safe('<br><b>Tipo IEU</b>: Inactivo')
            messages.error(self.request, mensaje)

        # Solo si no es un publicador desabilito las opciones de revisor
        if not self.request.user.has_perm('oeu.post_oeu'):
            self.fields['publicar'].disabled = True
            self.fields['cod_activacion'].disabled = True


##############################################################################
class SubTipoInstitucionForm(ModelForm):
    """
    Formulario ajustado para manipular los tipos de institución de la oferta académica
    """
    tipo_ieu = forms.CharField(disabled=True, label='Tipo IEU', required=False)
    nombre_sub_tipo = forms.CharField(disabled=True, label='Sub Tipo Institucion', required=False)
    orden = forms.CharField(disabled=True, label='Orden IEU', required=False)
    # usuario_revisor = forms.CharField(disabled=True, label='Revisor(es)', required=False)
    # usuario_editor = forms.CharField(disabled=True, label='Editor', required=False)
    # revisor_edit = forms.CharField(disabled=True, label='')
    cod_activacion = forms.ChoiceField(widget=forms.RadioSelect(), label='Activo/Inactivo')

    class Meta:
        model = SubTipoInstitucion
        fields = (
            'cod_activacion',
            'tipo_ieu_edit',
        )
        widgets = {
            'cod_activacion': widgets.RadioSelect(attrs={}),
            'tipo_ieu_edit': autocomplete.ModelSelect2(url='oeu:tipo-ieu', attrs={'data-placeholder':'Tipo IEU ...',},),
        }
        labels = {
            'tipo_ieu_edit': (''),
            'nombre_edit': (''),
            'orden_edit': (''),
            'revisor_edit': ('')
        }

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        super(SubTipoInstitucionForm, self).__init__(*args, **kwargs)

        # self.fields['revisor_edit'].widget.attrs['readonly'] = True

        # Concateno a los revisores
        # self.initial['revisor_edit'] = valida_editor(self, self.instance.revisor_edit)

        # Si estoy editando un registro incializo los campos
        if self.instance.pk:
            self.initial['nombre_sub_tipo'] = self.instance.nombre
            self.initial['tipo_ieu'] = self.instance.tipo_ieu
            self.initial['orden'] = self.instance.orden
            # self.initial['usuario_revisor'] = self.instance.revisor
            # self.initial['usuario_editor'] = self.instance.editor
            current_cod_activacion = self.instance.cod_activacion

            # Construyo su codigo de validadción de acuerdo al modelo (tabla) correspondiente
            # tratarse del modelo TipoInstitucion debemos controlar el bit 8 (posición 7 en la
            # lista) del cod_activacion.

            # Al guardar siempre se debe inactivar el bit de revisado (bit 2 posicion 1 en la lista)
            # para indicar que este registro fue revisado por alguien
            current_cod_activacion = list(current_cod_activacion)
            current_cod_activacion[1] ='0'
            current_cod_activacion = ''.join(current_cod_activacion)

            if current_cod_activacion[6:7] == '1':
                activo = current_cod_activacion
                inactivo = list(activo)
                inactivo[6] = '0'
                inactivo = ''.join(inactivo)
            else:
                inactivo = current_cod_activacion
                activo = list(inactivo)
                activo[6] = '1'
                activo = ''.join(activo)
        else:
            activo = '00000011'
            inactivo = '00000001'
            current_cod_activacion = activo

        CODACTIVACION = (
            (activo, 'Activo'),
            (inactivo, 'Inactivo')
        )

        self.fields['cod_activacion'].choices = CODACTIVACION
        self.initial['cod_activacion'] = current_cod_activacion

        # Preparar mensaje de inactivación:
        if current_cod_activacion != '01000011' and current_cod_activacion != '11000011' and current_cod_activacion != '10000011' and current_cod_activacion != '00000011' and self.instance.pk:
            mensaje = mark_safe('Este Sub Tipo IEU se encuentra inactivo:')
            if current_cod_activacion[7:8] == '0':
                mensaje += mark_safe('<br><b>Tipo IEU</b>: Inactivo' + activo[7:8] + activo[6:7])
            if current_cod_activacion[6:7] == '0':
                mensaje += mark_safe('<br><b>Sub Tipo Institucion</b>: Inactivo')
            messages.error(self.request, mensaje)

        # Solo si no es un publicador desabilito las opciones de revisor
        if not self.request.user.has_perm('oeu.post_oeu'):
            self.fields['publicar'].disabled = True
            self.fields['cod_activacion'].disabled = True


##############################################################################
class TipoIeuForm(ModelForm):
    """
    Formulario ajustado para manipular los tipos de institución de la oferta
    académica
    """
    class Meta:
        model = TipoInstitucion
        fields = (
            'nombre_edit',
            'cod_activacion',
            'orden_edit',
            'publicar',
            'editor',
        )
        labels = {
            'nombre_edit': 'Nombre',
            'orden_edit': 'Orden',
        }
        widgets = {
            'nombre_edit': forms.TextInput(attrs={'class':'form-control'}),
            'orden_edit': forms.NumberInput(attrs={'class':'form-control'}),
        }


##############################################################################
class TipoInstitucionSfcForm(ModelForm):
    class Meta:
        model = TipoInstitucionSfc
        exclude = ()


TIPOIEUSFC_FORMSET = inlineformset_factory(
    TipoInstitucion,
    TipoInstitucionSfc,
    fields=['sfc'],
    widgets={'sfc': forms.Select(attrs={'class':'form-control'})},
    form=TipoInstitucionSfcForm,
    extra=1
    )


##############################################################################
class SubTipoIeuForm(ModelForm):
    """
    Formulario ajustado para manipular los tipos de institución de la oferta
    académica
    """
    class Meta:
        model = SubTipoInstitucion
        fields = (
            'tipo_ieu_edit',
            'nombre_edit',
            'cod_activacion',
            'orden_edit',
            'publicar',
            'editor',
        )
        labels = {
            'tipo_ieu_edit': 'Tipo IEU',
            'nombre_edit': 'Nombre',
            'orden_edit': 'Orden',
        }
        widgets = {
            'tipo_ieu_edit': autocomplete.ModelSelect2(
                url='oeu:tipo-ieu-au',
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Tipo IEU ...',
                },
            ),
            'nombre_edit': forms.TextInput(attrs={'class':'form-control'}),
            'orden_edit': forms.NumberInput(attrs={'class':'form-control'}),
        }


##############################################################################
class SubTipoInstitucionSfcForm(ModelForm):
    class Meta:
        model = SubTipoInstitucionSfc
        exclude = ()


SUBTIPOIEUSFC_FORMSET = inlineformset_factory(
    SubTipoInstitucion,
    SubTipoInstitucionSfc,
    fields=['sfc'],
    widgets={'sfc': forms.Select(attrs={'class':'form-control'})},
    form=SubTipoInstitucionSfcForm,
    extra=1
    )

##############################################################################
class TipoEspecificoIeuForm(ModelForm):
    """
    Formulario ajustado para manipular los tipos de institución de la oferta
    académica
    """
    class Meta:
        model = TipoEspecificoInstitucion
        fields = (
            'tipo_ieu_edit',
            'sub_tipo_ieu_edit',
            'nombre_edit',
            'cod_activacion',
            'orden_edit',
            'publicar',
            'editor',
        )
        labels = {
            'tipo_ieu_edit': 'Tipo IEU',
            'sub_tipo_ieu_edit': 'Sub Tipo IEU',
            'nombre_edit': 'Nombre',
            'orden_edit': 'Orden',
        }
        widgets = {
            'tipo_ieu_edit': autocomplete.ModelSelect2(
                url='oeu:tipo-ieu-au',
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Tipo IEU ...',
                },
            ),
            'sub_tipo_ieu_edit': autocomplete.ModelSelect2(
                url='oeu:sub-tipo-ieu-au',
                forward=['tipo_ieu_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Sub Tipo IEU ...',
                },
            ),
            # 'sub_tipo_ieu_edit': forms.Select(attrs={'class':'form-control'}),
            'nombre_edit': forms.TextInput(attrs={'class':'form-control'}),
            'orden_edit': forms.NumberInput(attrs={'class':'form-control'}),
        }


##############################################################################
class TipoEspecificoIeuSfcForm(ModelForm):
    """
    Formulario ajustado para manipular los TipoEspecificoIeuSfcForm
    """
    class Meta:
        model = SubTipoInstitucionSfc
        exclude = ()


TIPOESPECIFICOIEUSFC_FORMSET = inlineformset_factory(
    TipoEspecificoInstitucion,
    TipoEspecificoIeuSfc,
    fields=['sfc'],
    widgets={'sfc': forms.Select(attrs={'class':'form-control'})},
    form=TipoEspecificoIeuForm,
    extra=1
    )

##############################################################################
class IeuForm(ModelForm):
    """
    Formulario ajustado para manipular las IEU de la oferta académica
    """
    class Meta:
        model = Ieu
        fields = (
            'tipo_ieu_edit',
            'sub_tipo_ieu_edit',
            'tipo_especifico_ieu_edit',
            'institucion_ministerial_edit',
            'localidad_principal_edit',
            'logo_edit',
            'fachada_edit',
            'cod_activacion',
            'publicar',
            'editor',
        )
        labels = {
            'tipo_ieu_edit': 'Tipo IEU',
            'sub_tipo_ieu_edit': 'Sub Tipo IEU',
            'tipo_especifico_ieu_edit': 'Tipo Específico',
            'institucion_ministerial_edit': 'Institución Ministerial',
            'localidad_principal_edit': 'Localidad Principal',
            'logo_edit': 'Logo',
            'fachada_edit': 'Fachada',
        }
        widgets = {
            'tipo_ieu_edit': autocomplete.ModelSelect2(
                url='oeu:tipo-ieu-au',
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Tipo IEU ...',
                },
            ),
            'sub_tipo_ieu_edit': autocomplete.ModelSelect2(
                url='oeu:sub-tipo-ieu-au',
                forward=['tipo_ieu_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Sub Tipo IEU ...',
                },
            ),
            'tipo_especifico_ieu_edit': autocomplete.ModelSelect2(
                url='oeu:tipo-especifico-ieu',
                forward=['sub_tipo_ieu_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Tipo Especifico IEU ...',
                },
            ),
            'institucion_ministerial_edit': autocomplete.ModelSelect2(
                url='globales:institucion-ministerial-ieu',
                forward=['tipo_especifico_ieu_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Institución Ministerial ...',
                },
            ),
            'localidad_principal_edit': autocomplete.ModelSelect2(
                url='oeu:localidad-ieu',
                forward=['institucion_ministerial_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Localidad Principal ...',
                },
            )
        }


##############################################################################
class IeuSfcForm(ModelForm):
    """
    Formulario ajustado para manipular las IeuSfcForm
    """
    class Meta:
        model = IeuSfc
        exclude = ()


IEUSFC_FORMSET = inlineformset_factory(
    Ieu,
    IeuSfc,
    fields=['sfc'],
    widgets={'sfc': forms.Select(attrs={'class':'form-control'})},
    form=IeuForm,
    extra=1
    )

##############################################################################
class LocalidadForm(ModelForm):
    """
    Formulario ajustado para manipular las IEU de la oferta académica
    """
    class Meta:
        model = Localidad
        fields = (
            'ieu_edit',
            'tipo_localidad_edit',
            'nombre_edit',
            'web_site_edit',
            'direccion_edit',
            'estado_edit',
            'municipio_edit',
            'parroquia_edit',
            'centro_poblado_edit',
            'coordenada_edit',
            'poligonal_edit',
            'fachada_edit',
            'cod_activacion',
            'publicar',
            'editor',
        )
        labels = {
            'ieu_edit': 'IEU',
            'tipo_localidad_edit': 'Tipo localidad',
            'nombre_edit': 'Nombre',
            'web_site_edit': 'Web',
            'estado_edit': 'Estado',
            'municipio_edit': 'Municipio',
            'parroquia_edit': 'Parroquia',
            'centro_poblado_edit': 'Centro poblado',
            'direccion_edit': 'Dirección',
            'coordenada_edit': 'Coordenada',
            'poligonal_edit': 'Poligonal',
            'fachada_edit': 'Fachada'
        }
        widgets = {
            'ieu_edit': autocomplete.ModelSelect2(
                url='oeu:ieu',
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'IEU ...',
                },
            ),
            'tipo_localidad_edit': forms.Select(attrs={'class':'form-control select2'}),
            'nombre_edit':  forms.TextInput(attrs={'class':'form-control'}),
            'web_site_edit': forms.URLInput(attrs={'class':'form-control'}),
            'direccion_edit': forms.Textarea(attrs={'class':'form-control', 'rows':2}),
            'estado_edit': autocomplete.ModelSelect2(
                url='globales:estadoAutoComplete',
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Estado ...',
                },
            ),
            'municipio_edit': autocomplete.ModelSelect2(
                url='globales:municipioAutoComplete',
                forward=['estado_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Estado ...',
                },
            ),
            'parroquia_edit': autocomplete.ModelSelect2(
                url='globales:parroquiaAutoComplete',
                forward=['municipio_edit'],
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Estado ...',
                },
            ),
            'centro_poblado_edit': forms.TextInput(attrs={'class':'form-control'}),
            'coordenada_edit': LeafletWidget(),
            'poligonal_edit': LeafletWidget(),
        }


##############################################################################
class LocalidadSfcForm(ModelForm):
    """
    Formulario ajustado para manipular las IeuSfcForm
    """
    class Meta:
        model = IeuSfc
        exclude = ()


LOCALIDADSFC_FORMSET = inlineformset_factory(
    Localidad,
    LocalidadSfc,
    fields=['sfc'],
    widgets={'sfc': forms.Select(attrs={'class':'form-control'})},
    form=LocalidadForm,
    extra=1
    )
