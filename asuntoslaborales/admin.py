# -*- coding: utf-8
"""
"""
# Librerias Django
# Django Library
from django.contrib import admin

# Librerias de terceros
# Thirdparty Library
from asuntoslaborales.models import (
    Cargo, Categoria, Dedicacion, HistoriaLaboral, HlCategoria, HlDedicacion,
    HlDesembolso, HlPermiso, HlSalarioIntegralAnual, Prima, SueldoBasico,
    TasaInteres, TipoCategoria, TipoPermiso, TipoPersonal)

# Librerias desarrolladas por mi
# Desarrolladas por mi
# from .forms import TipoInstitucionForm, InstitucionForm, LocalidadForm,\
#     SFCForm, AreaConocimientoForm, SubAreaConocimientoForm, CarreraForm
from opsu.actions import export_as_csv_action

# Librerias en carpetas locales
# Localfolder Library
from .forms import HistoriaLaboralForm


def duplicate_event(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_event.short_description = "Duplicar Registro Seleccionado"



###############################################################################
@admin.register(TipoPersonal)
class TipoPersonalAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se dictan en las localidades
    de las IEU
    """
    search_fields = ['nombre_tipo_personal',]
    list_display = ['nombre_tipo_personal',]
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los cargos del personal de las IEU
    """
    search_fields = ['nombre_cargo',]
    list_display = ['id_tipo_personal', 'nombre_cargo',]
    list_display_links = ['id_tipo_personal', 'nombre_cargo',]
    ordering = ['id_tipo_personal', 'nombre_cargo',]
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(Dedicacion)
class DedicacionAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los cargos del personal de las IEU
    """
    search_fields = ['nombre_dedicacion',]
    list_display = ['id_tipo_personal', 'id_cargo', 'nombre_dedicacion',]
    list_display_links = ['id_tipo_personal', 'id_cargo', 'nombre_dedicacion',]
    ordering = ['id_tipo_personal', 'id_cargo', 'nombre_dedicacion',]
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(SueldoBasico)
class SueldoBasicoAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los cargos del personal de las IEU
    """
    # search_fields = ['sueldo',]
    list_filter = ['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion',]
    list_display = ['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion', 'sueldo',]
    list_display_links = [
        'id_institucion',
        'id_tipo_personal',
        'cargo',
        'dedicacion',
        'sueldo',
    ]
    actions = [duplicate_event, export_as_csv_action("Exportar Sueldos Básicos Seleccionados", fields=['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion', 'desde', 'hasta', 'sueldo',])]
    ordering = ['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion', 'sueldo',]
    localized_fields = '__all__'
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(Prima)
class PrimaAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los cargos del personal de las IEU
    """
    # search_fields = ['monto_prima',]
    list_filter = ['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion',]
    list_display = ['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion', 'nombre_prima', 'monto_prima',]
    list_display_links = [
        'id_institucion',
        'id_tipo_personal',
        'cargo',
        'dedicacion',
        'nombre_prima',
        'monto_prima',
    ]
    actions = [duplicate_event]
    ordering = ['id_institucion', 'id_tipo_personal', 'cargo', 'dedicacion', 'nombre_prima', 'monto_prima',]
    localized_fields = '__all__'
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True


#### Inlines para la HL ####
class HlCategoriaInline(admin.TabularInline):
    model = HlCategoria
    extra = 1


class HlDedicacionInline(admin.TabularInline):
    model = HlDedicacion
    extra = 1


class HlPermisoInline(admin.TabularInline):
    model = HlPermiso
    extra = 1


class HlDesembolsoInline(admin.TabularInline):
    model = HlDesembolso
    extra = 1


class HlSalarioIntegralAnualInline(admin.TabularInline):
    model = HlSalarioIntegralAnual
    extra = 1


###############################################################################
@admin.register(HistoriaLaboral)
class HistoriaLaboralAdmin(admin.ModelAdmin):
    """
    """
    form = HistoriaLaboralForm
    show_full_result_count = True
    actions_selection_counter = True
    inlines = [HlCategoriaInline, HlDedicacionInline, HlPermisoInline, \
    HlDesembolsoInline, HlSalarioIntegralAnualInline,]


###############################################################################
@admin.register(HlDesembolso)
class HlDesembolsoAdmin(admin.ModelAdmin):
    """
    """

    list_filter = ['historia_laboral', 'fecha', 'monto', 'tipo_desembolso',]
    list_display = ['historia_laboral', 'fecha', 'monto', 'tipo_desembolso',]
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(HlCategoria)
class HlCategoriaAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(HlDedicacion)
class HlDedicacionAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(HlPermiso)
class HlPermisoAdmin(admin.ModelAdmin):
    """
    """
    list_filter = ['historia_laboral', 'fecha_inicio', 'fecha_fin', 'tipo_permiso', 'descuenta',]
    list_display = ['historia_laboral', 'fecha_inicio', 'fecha_fin', 'tipo_permiso', 'descuenta',]
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(HlSalarioIntegralAnual)
class HlSalarioIntegralAnualAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(TasaInteres)
class TasaInteresAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(TipoCategoria)
class TipoCategoriaAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True


###############################################################################
@admin.register(TipoPermiso)
class TipoPermisoAdmin(admin.ModelAdmin):
    """
    """
    show_full_result_count = True
    actions_selection_counter = True
