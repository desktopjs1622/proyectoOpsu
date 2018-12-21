# Librerias Django
from django.contrib import admin
from django.utils.safestring import mark_safe

# Librerias de terceros
from oeuconfig.forms import SfcForm
from oeuconfig.models import (
    ActividadCultural, AgrupacionCivica, AyudaEconomica, DisciplinaDeportiva,
    InstanciaAdministrativa, Modalidad, OrganizacionEstudiantil, RedSocial,
    RequisitoIngreso, Servicio, SoporteFormalCambio, TipoCarrera,
    TipoLocalidad, TipoSoporteFormalCambio, TipoTurnoDeEstudio, Titulo)

# Librerias desarrolladas por mi
from opsu.actions import export_as_csv_action


@admin.register(TipoTurnoDeEstudio)
class TurnoAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los turnos en las IEU
    """
    search_fields = ['nombre', ]
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(RequisitoIngreso)
class RequisitoIngresoAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    search_fields = ['requisito_ingreso', ]
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    search_fields = ['nombre', ]
    show_full_result_count = True
    actions_selection_counter = True
    list_display = [
        'nombre',
        'link_relacionado',
    ]

    def link_relacionado(self, obj):
        url = '../localidad/?q=&servicio__id_servicio__exact='
        url_link = 'Ver Localidades con este Servicio'
        return mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_servicio, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Localidades con este Servicio'


@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    search_fields = ['nombre', ]
    list_display = [
        'nombre',
        'link_relacionado',
    ]
    actions = [export_as_csv_action("Exportar Títulos Seleccionados", fields=[
                                    'id_titulo', 'nombre', ])]
    show_full_result_count = True
    actions_selection_counter = True

    def link_relacionado(self, obj):
        url = '../carrera/?q=&id_titulo_pub__id_titulo__exact='
        url_link = 'Ver Programas que Otorgan este Título'
        return mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_titulo, url_link))

    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Programas que Otorgan este Título'


@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    search_fields = ['nombre', ]
    list_display = [
        'nombre',
        'link_relacionado',
    ]
    show_full_result_count = True
    actions_selection_counter = True

    def link_relacionado(self, obj):
        url = '../carrera/?q=&id_modalidad_pub__id_modalidad__exact='
        url_link = 'Ver Programas con este Régimen de Estudio'
        return mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_modalidad, url_link))

    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Programas con este Régimen de Estudio'


@admin.register(TipoCarrera)
class TipoCarreraAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    search_fields = ['nombre', ]
    list_display = ['nombre', 'link_relacionado', ]
    show_full_result_count = True
    actions_selection_counter = True

    def link_relacionado(self, obj):
        url = '../carrera/?id_tipo_carrera_pub__id_tipo_carrera__exact='
        url_link = 'Ver Carreras de este tipo'
        return mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_tipo_carrera, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Carreras de este tipo'


@admin.register(InstanciaAdministrativa)
class InstanciaAdministrativaAdmin(admin.ModelAdmin):
    """
    Con esta clase se pueden controlar las instancias administrativas de
    las localidades de las IEU
    """
    fields = ['nombre', 'publicar', ]
    search_fields = ['nombre', ]
    list_display = ['nombre', 'publicar', ]
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(TipoSoporteFormalCambio)
class TipoSoporteFormalCambioAdmin(admin.ModelAdmin):
    fields = [
        'nombre',
    ]
    search_fields = ['nombre', ]
    list_display = ['nombre', 'link_relacionado', ]
    show_full_result_count = True
    actions_selection_counter = True

    def link_relacionado(self, obj):
        url = '../soporteformalcambio/?q=&id_tipo_sfc__id_tipo_sfc__exact='
        url_link = 'Ver SFC de este tipo'
        return mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_tipo_sfc, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'SFC de este tipo'


@admin.register(SoporteFormalCambio)
class SFCAdmin(admin.ModelAdmin):
    form = SfcForm
    search_fields = ['nombre', ]
    list_display = ['nombre', 'tipo_sfc', ]
    list_filter = ['tipo_sfc', ]
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(TipoLocalidad)
class TipoLocalidadAdmin(admin.ModelAdmin):
    fields = [
        'nombre',
        'descripcion',
    ]
    search_fields = ['nombre', ]
    list_display = ['nombre', 'link_relacionado', ]
    show_full_result_count = True
    actions_selection_counter = True

    def link_relacionado(self, obj):
        url = '../localidad/?q=&id_tipo_localidad__id_tipo_localidad__exact='
        url_link = 'Ver Localidades de este tipo'
        return mark_safe('<a href="%s%s">%s</a>' % (url, obj.tipo_localidad, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Localidades de este tipo'


@admin.register(AyudaEconomica)
class AyudaEconomicaAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(ActividadCultural)
class ActividadCulturalAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(DisciplinaDeportiva)
class DisciplinaDeportivaAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(OrganizacionEstudiantil)
class OrganizacionEstudiantilAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(AgrupacionCivica)
class AgrupacionCivicaAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    show_full_result_count = True
    actions_selection_counter = True


@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    """
    Con esta clase Admin se pueden controlar los tipos de carrera que se
    dictan en las localidades de las IEU
    """
    show_full_result_count = True
    actions_selection_counter = True
