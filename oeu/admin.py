"""Admin para las instancias sustantivas del LOEU
"""
# Librerias Django
from django.contrib import admin
from django.db.models import Q
from django.urls import reverse
from django.utils.safestring import mark_safe

# Librerias de terceros
from leaflet.admin import LeafletGeoAdmin

# Librerias desarrolladas por mi
from oeu.models import (
    ActividadCulturalLocalidad, AgrupacionCivicaLocalidad, AreaConocimiento,
    AyudaEconomicaLocalidad, Carrera, CorreoLocalidad,
    DisciplinaDeportivaLocalidad, Ieu, Localidad,
    OrganizacionEstudiantilLocalidad, RedSocialLocalidad, SubAreaConocimiento,
    SubTipoInstitucion, TelefonoLocalidad, TipoInstitucion, TipoInstitucionSfc)
from opsu.actions import export_as_csv_action

# Librerias en carpetas locales
from .forms import SubTipoInstitucionForm, TipoInstitucionForm

admin.site.register(Localidad, LeafletGeoAdmin)


##############################################################################
class CodActTipoFilter(admin.SimpleListFilter):
    title = 'Estatus'
    parameter_name = 'codact'

    def lookups(self, request, model_admin):
        codigo_act = [
            ('todo', 'Todo'),
            ('revisado', 'Revisado'),
            ('activo', 'Activo'),
            ('nuevo', 'Nuevo'),
            ('inactivo', 'Inactivo')]
        return codigo_act

    def queryset(self, request, queryset):
        """Activo = Todos lo que el bit 0 encendido y el bit 7 encendido (Solo
        los públicados aunque esten en revisión)
        """
        if self.value() == 'activo' or self.value() is None:
            return queryset.filter(Q(cod_activacion__exact='11000001') | Q(cod_activacion__exact='10000001'))

        # Todos los que el bit 0 encendido, el bit 1 apagado y el bit 7 encendido (Solo los públicados en proceso de revisión)
        elif self.value() == 'revisado':
            return queryset.filter(cod_activacion='10000001')

        # Todos los que tienen el bit 0 apagado, el bit 1 apagado y bit 7 encendido (nuevos registros)
        elif self.value() == 'nuevo':
            return queryset.filter(Q(cod_activacion='00000001'))

        elif self.value() == 'inactivo':
            return queryset.filter(~Q(cod_activacion__exact='11000001'), ~Q(cod_activacion__exact='10000001'), ~Q(cod_activacion__exact='00000001'))
        else:
            return queryset


##############################################################################
class CodActEspecFilter(admin.SimpleListFilter):
    title = 'Estatus'
    parameter_name = 'codact'

    def lookups(self, request, model_admin):
        codigo_act = [('todo', 'Todo'), ('revisado', 'Revisado'), ('activo', 'Activo'), ('nuevo', 'Nuevo'), ('inactivo', 'Inactivo')]
        return codigo_act

    def queryset(self, request, queryset):
        # Activo = Todos lo que el bit 0, 6 y 7 encendido (Solo los públicados aunque esten en revisión)
        if self.value() == 'activo' or self.value() is None:
            return queryset.filter(Q(cod_activacion__exact='11000011') | Q(cod_activacion__exact='10000011'))

        # Todos los que el bit 0 encendido, el bit 1 apagado y el bit 6 y 7 encendido (Solo los públicados en proceso de revisión)
        elif self.value() == 'revisado':
            return queryset.filter(cod_activacion='10000011')

        # Todos los que tienen el bit 0 apagado, el bit 1 apagado y bit 6 y 7 encendido (nuevos registros)
        elif self.value() == 'nuevo':
            return queryset.filter(Q(cod_activacion='00000011') | Q(cod_activacion='00000001'))

        elif self.value() == 'inactivo':
            return queryset.filter(~Q(cod_activacion__exact='11000011'), ~Q(cod_activacion__exact='10000011'), ~Q(cod_activacion__exact='00000011'), ~Q(cod_activacion__exact='00000001'))
        else:
            return queryset


##############################################################################
class CodActDetalFilter(admin.SimpleListFilter):
    title = 'Estatus'
    parameter_name = 'codact'

    def lookups(self, request, model_admin):
        codigo_act = [('todo', 'Todo'), ('revisado', 'Revisado'), ('activo', 'Activo'), ('nuevo', 'Nuevo'), ('inactivo', 'Inactivo')]
        return codigo_act

    def queryset(self, request, queryset):
        # Activo = Todos lo que el bit 0, 5, 6 y 7 encendido (Solo los públicados aunque esten en revisión)
        if self.value() == 'activo' or self.value() is None:
            return queryset.filter(Q(cod_activacion__exact='11000111') | Q(cod_activacion__exact='10000111'))

        # Todos los que el bit 0 encendido, el bit 1 apagado y el bit 5, 6 y 7 encendido (Solo los públicados en proceso de revisión)
        elif self.value() == 'revisado':
            return queryset.filter(cod_activacion='10000111')

        # Todos los que tienen el bit 0 apagado, el bit 1 apagado y bit 5, 6 y 7 encendido (nuevos registros)
        elif self.value() == 'nuevo':
            return queryset.filter(Q(cod_activacion='00000111') | Q(cod_activacion='00000011'))

        elif self.value() == 'inactivo':
            return queryset.filter(~Q(cod_activacion__exact='11000111'), ~Q(cod_activacion__exact='10000111'), ~Q(cod_activacion__exact='00000111'), ~Q(cod_activacion__exact='00000011'))
        else:
            return queryset


##############################################################################
class CodActInstFilter(admin.SimpleListFilter):
    title = 'Estatus'
    parameter_name = 'codact'

    def lookups(self, request, model_admin):
        codigo_act = [('todo', 'Todo'), ('revisado', 'Revisado'), ('activo', 'Activo'), ('nuevo', 'Nuevo'), ('inactivo', 'Inactivo')]
        return codigo_act

    def queryset(self, request, queryset):
        # Activo = Todos lo que el bit 0, 4, 5, 6 y 7 encendido (Solo los públicados aunque esten en revisión)
        if self.value() == 'activo' or self.value() is None:
            return queryset.filter(Q(cod_activacion__exact='11001111') | Q(cod_activacion__exact='10001111'))

        # Todos los que el bit 0 encendido, el bit 1 apagado y el bit 4, 5, 6 y 7 encendido (Solo los públicados en proceso de revisión)
        elif self.value() == 'revisado':
            return queryset.filter(cod_activacion='10001111')

        # Todos los que tienen el bit 0 apagado, el bit 1 apagado y bit 4, 5, 6 y 7 encendido (nuevos registros)
        elif self.value() == 'nuevo':
            return queryset.filter(Q(cod_activacion='00001111') | Q(cod_activacion='00000111'))

        elif self.value() == 'inactivo':
            return queryset.filter(~Q(cod_activacion__exact='11001111'), ~Q(cod_activacion__exact='10001111'), ~Q(cod_activacion__exact='00001111'), ~Q(cod_activacion__exact='00000111'))
        else:
            return queryset


##############################################################################
class CodActLocaFilter(admin.SimpleListFilter):
    title = 'Estatus'
    parameter_name = 'codact'

    def lookups(self, request, model_admin):
        codigo_act = [('todo', 'Todo'), ('revisado', 'Revisado'), ('activo', 'Activo'), ('nuevo', 'Nuevo'), ('inactivo', 'Inactivo')]
        return codigo_act

    def queryset(self, request, queryset):
        # Activo = Todos lo que el bit 0, 4, 5, 6 y 7 encendido (Solo los públicados aunque esten en revisión)
        if self.value() == 'activo' or self.value() is None:
            return queryset.filter(Q(cod_activacion__exact='11011111') | Q(cod_activacion__exact='10011111'))

        # Todos los que el bit 0 encendido, el bit 1 apagado y el bit 4, 5, 6 y 7 encendido (Solo los públicados en proceso de revisión)
        elif self.value() == 'revisado':
            return queryset.filter(cod_activacion='10011111')

        # Todos los que tienen el bit 0 apagado, el bit 1 apagado y bit 4, 5, 6 y 7 encendido (nuevos registros)
        elif self.value() == 'nuevo':
            return queryset.filter(Q(cod_activacion='00011111') | Q(cod_activacion='00001111'))

        elif self.value() == 'inactivo':
            return queryset.filter(~Q(cod_activacion__exact='11011111'), ~Q(cod_activacion__exact='10011111'), ~Q(cod_activacion__exact='00011111'), ~Q(cod_activacion__exact='00001111'))
        else:
            return queryset


##############################################################################
class CodActCarrFilter(admin.SimpleListFilter):
    title = 'Estatus'
    parameter_name = 'codact'

    def lookups(self, request, model_admin):
        codigo_act = [('todo', 'Todo'), ('revisado', 'Revisado'), ('activo', 'Activo'), ('nuevo', 'Nuevo'), ('inactivo', 'Inactivo')]
        return codigo_act

    def queryset(self, request, queryset):
        # Activo = Todos los registros que el bit 0, 2, 3, 4, 5, 6 y 7 encendido (Solo los públicados aunque esten en revisión)
        if self.value() == 'activo' or self.value() is None:
            return queryset.filter(Q(cod_activacion__exact='11111111') | Q(cod_activacion__exact='10111111'))

        # Todos los registros en los que el bit 0 encendido, el bit 1 apagado y el bit 2, 3, 4, 5, 6 y 7 encendido (Solo los públicados en proceso de revisión)
        elif self.value() == 'revisado':
            return queryset.filter(cod_activacion='10111111')

        # Todos los que tienen el bit 0 apagado, el bit 1 apagado y bit 3, 4, 5, 6 y 7 encendido (nuevos registros activos o inactivos)
        elif self.value() == 'nuevo':
            return queryset.filter(Q(cod_activacion='00111111') | Q(cod_activacion='00011111'))

        elif self.value() == 'inactivo':
            return queryset.filter(~Q(cod_activacion__exact='11111111'), ~Q(cod_activacion__exact='10111111'), ~Q(cod_activacion__exact='00111111'), ~Q(cod_activacion__exact='00011111'))
        else:
            return queryset

##############################################################################
@admin.register(TipoInstitucionSfc)
class ArchivoInline(admin.ModelAdmin):
    model = TipoInstitucionSfc
    extra = 1


##############################################################################
class SfcTipoInstitucionInline(admin.TabularInline):
    model = TipoInstitucion.sfc.through
    extra = 1
    verbose_name = "Soporte Formal de Cambio"
    verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
@admin.register(TipoInstitucion)
class TipoInstitucionAdmin(admin.ModelAdmin):
    fields = [
        ('nombre_tipo', 'nombre_edit',),
        ('orden', 'orden_edit',),
        # ('usuario_revisor',),
        # 'usuario_editor',
        'publicar',
        'cod_activacion',
        # 'activacion',
    ]
    form = TipoInstitucionForm
    search_fields = ['nombre',]
    list_display = ['nombre', 'link_relacionado',]
    list_filter = [CodActTipoFilter,]
    ordering = ['nombre',]
    actions = [export_as_csv_action("Exportar los Tipos de IEU seleccionados",)]
    show_full_result_count = True
    actions_selection_counter = True
    inlines = [SfcTipoInstitucionInline,]

    def get_form(self, request, obj=None, **kwargs):

        ModelForm = super(TipoInstitucionAdmin, self).get_form(request, obj, **kwargs)

        class ModelFormMetaClass(ModelForm):
            def __new__(cls, *args, **kwargs):
                kwargs['request'] = request
                return ModelForm(*args, **kwargs)
        return ModelFormMetaClass

    def link_relacionado(self, obj):
        url = '../subtipoinstitucion/?q=&tipo_ieu__tipo_ieu__exact='
        url_link = 'Ver Sub Tipos'
        return  mark_safe('<a href="%s%s">%s</a>' % (url, obj.pk, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'IEU de este tipo'

    def suit_row_attributes(self, obj):
        css_class = {
            '11000001': 'success', # Activo y públicado
            '10000001': 'info', # Activo públicado en proceso de revisión
            '00000001': 'warning', # Nuevo registro en revision sin publicar
            '00000000': 'error', # Nuevo registro inactivo en revision sin publicar
        }.get(obj.cod_activacion)
        if css_class == 'success':
            return {'class': css_class, 'data': obj.cod_activacion}
        if css_class == 'info':
            return {'class': css_class, 'data': obj.cod_activacion}
        if css_class == 'warning':
            return {'class': css_class, 'data': obj.cod_activacion}
        else:
            return {'class': 'error', 'data': obj.cod_activacion}

    def save_model(self, request, obj, form, change):
        if obj.publicar:
            obj.editor = request.user.username
        super(TipoInstitucionAdmin, self).save_model(request, obj, form, change)


##############################################################################
class SfcSubTipoInstitucionInline(admin.TabularInline):
    model = SubTipoInstitucion.sfc.through
    extra = 1
    verbose_name = "Soporte Formal de Cambio"
    verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
@admin.register(SubTipoInstitucion)
class SubTipoInstitucionAdmin(admin.ModelAdmin):
    fields = [
        ('tipo_ieu', 'tipo_ieu_edit',),
        ('nombre_sub_tipo', 'nombre_edit',),
        ('orden', 'orden_edit',),
        # ('usuario_revisor',),
        # 'usuario_editor',
        'publicar',
        'cod_activacion',
    ]
    form = SubTipoInstitucionForm
    search_fields = ['tipo_ieu', 'nombre',]
    list_filter = ['tipo_ieu', CodActEspecFilter,]
    list_display = ['link_personalizado', 'link_relacionado',]
    ordering = ['tipo_ieu', 'nombre',]
    actions = [export_as_csv_action("Exportar los Sub Tipos de IEU",)]
    # list_display_links = ['tipo_ieu', 'nombre_tipo_especifico_pub',]
    show_full_result_count = True
    actions_selection_counter = True
    inlines = [SfcSubTipoInstitucionInline,]
    list_select_related = False

    def get_form(self, request, obj=None, **kwargs):

        ModelForm = super(SubTipoInstitucionAdmin, self).get_form(request, obj, **kwargs)

        class ModelFormMetaClass(ModelForm):
            def __new__(cls, *args, **kwargs):
                kwargs['request'] = request
                return ModelForm(*args, **kwargs)
        return ModelFormMetaClass

    def link_relacionado(self, obj):
        url = '../TipoEspecificoInstitucion/?q=&sub_tipo_ieu__id_tipo_ieu_especifico__exact='
        url_link = 'Ver Tipo Especifco de IEU'
        return  mark_safe('<a href="%s%s">%s</a>' % (url, obj.pk, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Detalle de este Sub Tipo Institucion de IEU'

    def link_personalizado(self, obj):
        url = reverse('admin:%s_%s_change' %(obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        url_link = '%s %s' % (obj.tipo_ieu, obj.nombre)
        return mark_safe('<a href="%s">%s</a>' % (url, url_link))
    link_personalizado.allow_tags = True
    link_personalizado.short_description = 'Sub Tipo Institucion de IEU'

    def suit_row_attributes(self, obj):
        css_class = {
            '11000011': 'success', # Activo y públicado
            '10000011': 'info', # Activo públicado en proceso de revisión
            '00000011': 'warning', # Nuevo registro en revision publicar
            '00000001': 'warning', # Nuevo registro en revision sin publicar
        }.get(obj.cod_activacion)
        if css_class == 'success':
            return {'class': css_class, 'data': obj.cod_activacion}
        if css_class == 'info':
            return {'class': css_class, 'data': obj.cod_activacion}
        if css_class == 'warning':
            return {'class': css_class, 'data': obj.cod_activacion}
        else:
            return {'class': 'error', 'data': obj.cod_activacion}

    def save_model(self, request, obj, form, change):
        if obj.publicar:
            obj.editor = request.user.username
        super(SubTipoInstitucionAdmin, self).save_model(request, obj, form, change)


##############################################################################
# class SfcTipoInstitucionDetallenline(admin.TabularInline):
#     model = TipoEspecificoInstitucion.sfc.through
#     extra = 1
#     verbose_name = "Soporte Formal de Cambio"
#     verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
# @admin.register(TipoEspecificoInstitucion)
# class TipoInstitucionDetalleAdmin(admin.ModelAdmin):
#     fields = [
#         ('tipo_ieu', 'tipo_ieu_edit',),
#         ('tipo_ieu_especifico', 'sub_tipo_ieu',),
#         ('nombre_tipo_detalle', 'nombre_tipo_detalle_edit',),
#         ('orden', 'orden_edit',),
#         ('usuario_revisor',),
#         'usuario_editor',
#         'publicar',
#         'cod_activacion',
#     ]
#     form = TipoInstitucionDetalleForm
#     search_fields = [
#         'tipo_ieu',
#         'sub_tipo_ieu',
#         'nombre',
#     ]
#     list_filter = ['tipo_ieu', 'sub_tipo_ieu', CodActDetalFilter]
#     list_display = ['link_personalizado', 'link_relacionado',]
#     ordering = [
#         'tipo_ieu',
#         'sub_tipo_ieu',
#         'nombre',
#     ]
#     actions = [export_as_csv_action("Exportar los Detalles de Tipos de IEU",)]
#     show_full_result_count = True
#     actions_selection_counter = True
#     # inlines = [SfcTipoInstitucionDetallenline,]

#     def get_form(self, request, obj=None, **kwargs):

#         ModelForm = super(TipoInstitucionDetalleAdmin, self).get_form(request, obj, **kwargs)

#         class ModelFormMetaClass(ModelForm):
#             def __new__(cls, *args, **kwargs):
#                 kwargs['request'] = request
#                 return ModelForm(*args, **kwargs)
#         return ModelFormMetaClass

#     def link_relacionado(self, obj):
#         url = '../institucion/?q=&id_tipo_ieu_especifico_pub__id_tipo_ieu_especifico__exact='
#         url_link = 'Ver Instituciones de Este Tipo Detalle de IEU'
#         return mark_safe('<a href="%s%s">%s</a>' % (url, obj.pk, url_link))
#     link_relacionado.allow_tags = True
#     link_relacionado.short_description = 'Detalle de este Sub Tipo Institucion de IEU'

#     def link_personalizado(self, obj):
#         url = reverse('admin:%s_%s_change' %(obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
#         url_link = '%s %s' % (obj.sub_tipo_ieu, obj.nombre)
#         return mark_safe('<a href="%s">%s</a>' % (url, url_link))

#     link_personalizado.allow_tags = True
#     link_personalizado.short_description = 'Detalle de este Sub Tipo Institucion de IEU'

#     def suit_row_attributes(self, obj):
#         css_class = {
#             '11000111': 'success', # Activo y públicado
#             '10000111': 'info', # Activo públicado en proceso de revisión
#             '00000111': 'warning', # Nuevo registro en revision sin publicar
#             '00000011': 'warning', # Nuevo registro inactivo en revision sin publicar
#         }.get(obj.cod_activacion)
#         if css_class == 'success':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'info':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'warning':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         else:
#             return {'class': 'error', 'data': obj.cod_activacion}

#     def save_model(self, request, obj, form, change):
#         if obj.publicar:
#             obj.editor = request.user.username
#         super(TipoInstitucionDetalleAdmin, self).save_model(request, obj, form, change)



# ##############################################################################
# class SfcInstitucionInline(admin.TabularInline):
#     model = Institucion.sfc.through
#     extra = 1
#     verbose_name = "Soporte Formal de Cambio"
#     verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
# @admin.register(Institucion)
# class InstitucionAdmin(admin.ModelAdmin):
#     fields = [
#         'cod_institucion',
#         ('nombre_institucion', 'nombre_institucion_edit',),
#         ('siglas', 'siglas_edit',),
#         ('dependencia_administrativa', 'id_dependencia_administrativa_edit',),
#         ('tipo_ieu', 'tipo_ieu_edit',),
#         ('sub_tipo_ieu', 'sub_tipo_ieu_edit',),
#         ('tipo_ieu_especifico', 'id_tipo_especifico_ieu_edit',),
#         # ('rif', 'rif_edit',),
#         ('localidad_principal', 'cod_localidad_principal_edit',),
#         ('usuario_revisor',),
#         'usuario_editor',
#         'publicar',
#         'cod_activacion',
#     ]
#     form = InstitucionForm
#     search_fields = ['nombre', 'siglas',]
#     list_filter = [
#         'dependencia_administrativa',
#         'tipo_ieu',
#         'sub_tipo_ieu',
#         'id_tipo_especifico_ieu',
#         'siglas',
#         CodActInstFilter,
#     ]
#     list_display = [
#         'id_tipo_especifico_ieu',
#         'nombre',
#         'dependencia_administrativa',
#         'link_relacionado',
#     ]
#     list_display_links = [
#         'tipo_ieu_especifico',
#         'nombre',
#         'dependencia_administrativa',
#     ]
#     ordering = ['tipo_ieu', 'nombre',]
#     actions = [export_as_csv_action("Exportar Instituciones Seleccionadas",)]
#     show_full_result_count = True
#     actions_selection_counter = True
#     inlines = [SfcInstitucionInline,]

#     def get_form(self, request, obj=None, **kwargs):

#         ModelForm = super(InstitucionAdmin, self).get_form(request, obj, **kwargs)

#         class ModelFormMetaClass(ModelForm):
#             def __new__(cls, *args, **kwargs):
#                 kwargs['request'] = request
#                 return ModelForm(*args, **kwargs)
#         return ModelFormMetaClass

#     def link_relacionado(self, obj):
#         url = '../localidad/?q=&id_institucion_pub__id_institucion__exact='
#         url_link = 'Ver localidades de esta IEU'
#         return mark_safe("<a href='%s%s'>%s</a>" % (url, obj.id_institucion, url_link))
#     link_relacionado.allow_tags = True
#     link_relacionado.short_description = 'Localidades de esta IEU'

#     def suit_row_attributes(self, obj):
#         css_class = {
#             '11001111': 'success', # Activo y públicado
#             '10001111': 'info', # Activo públicado en proceso de revisión
#             '00001111': 'warning', # Nuevo registro en revision sin publicar
#             '00000111': 'warning', # Nuevo registro inactivo en revision sin publicar
#         }.get(obj.cod_activacion)
#         if css_class == 'success':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'info':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'warning':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         else:
#             return {'class': 'error', 'data': obj.cod_activacion}

#     def save_model(self, request, obj, form, change):
#         if obj.publicar:
#             obj.editor = request.user.username
#         super(InstitucionAdmin, self).save_model(request, obj, form, change)


# ##############################################################################
# class SfcLocalidadInline(admin.TabularInline):
#     model = Localidad.sfc.through
#     extra = 1
#     verbose_name = "Soporte Formal de Cambio"
#     verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
class TelefonoLocalidadInline(admin.TabularInline):
    model = TelefonoLocalidad
    fields = [
        'id_instancia_administrativa',
        'numero_telefono',
    ]
    extra = 1


##############################################################################
class CorreoLocalidadInline(admin.TabularInline):
    model = CorreoLocalidad
    classes = ['collapse']
    fields = [
        'id_instancia_administrativa',
        'correo',
    ]
    extra = 1


##############################################################################
class AyudaEconomicaLocalidadInline(admin.TabularInline):
    model = AyudaEconomicaLocalidad
    fields = [
        'id_instancia_administrativa',
        'numero_telefono',
        'id_ayuda_economica',
    ]
    extra = 1


##############################################################################
class ActividadCulturalLocalidadInline(admin.TabularInline):
    model = ActividadCulturalLocalidad
    fields = [
        'id_instancia_administrativa',
        'numero_telefono',
        'id_actividad_cultural',
    ]
    extra = 1


##############################################################################
class DisciplinaDeportivaLocalidadInline(admin.TabularInline):
    model = DisciplinaDeportivaLocalidad
    fields = [
        'id_instancia_administrativa',
        'numero_telefono',
        'id_disciplina_eportiva',
    ]
    extra = 1


##############################################################################
class OrganizacionEstudiantilLocalidadInline(admin.TabularInline):
    model = OrganizacionEstudiantilLocalidad
    fields = [
        'id_instancia_administrativa',
        'numero_telefono',
        'id_organizacion_estudiantil',
    ]
    extra = 1


##############################################################################
class AgrupacionCivicaLocalidadInline(admin.TabularInline):
    model = AgrupacionCivicaLocalidad
    fields = [
        'id_instancia_administrativa',
        'numero_telefono',
        'id_agrupacion_civica',
    ]
    extra = 1


##############################################################################
class RedSocialLocalidadInline(admin.TabularInline):
    model = RedSocialLocalidad
    fields = [
        'id_instancia_administrativa',
        'id_red_social',
        'identificador',
    ]
    extra = 1


##############################################################################
# class RequisitoIngresoInline(admin.TabularInline):
#     model = Localidad.requisito_ingreso.through
#     extra = 1
#     verbose_name = "Requisto de Ingreso"
#     verbose_name_plural = "Requistos de Ingresos"


##############################################################################
# class ServiciosInline(admin.TabularInline):
#     model = Localidad.servicio.through
#     extra = 1
#     verbose_name = "Servicio"
#     verbose_name_plural = "Servicios"


##############################################################################
# @admin.register(Localidad)
# class LocalidadAdmin(admin.ModelAdmin):
#     fields = [
#         ('ieu', 'id_institucion_edit',),
#         ('tipo', 'id_tipo_localidad_edit',),
#         ('nombre', 'nombre_localidad_edit',),
#         ('web', 'web_site_localidad_edit',),
#         ('direccion', 'direccion_localidad_edit',),
#         ('estado', 'estado_edit',),
#         ('municipio', 'municipio_edit',),
#         ('parroquia', 'parroquia_edit',),
#         ('centro_poblado', 'centro_poblado_edit',),
#         ('coordenadas', 'coordenada_geografica_edit',),
#         ('poligonal', 'poligonal_geografica_edit',),
#         ('usuario_revisor', 'revisor_edit'),
#         'usuario_editor',
#         'publicar',
#         'cod_activacion',
#         'requisito_ingreso',
#         'servicio',
#     ]
#     form = LocalidadForm
#     search_fields = ['nombre',]
#     list_filter = ['institucion', 'nombre', 'estado', CodActLocaFilter,]
#     list_display = [
#         'institucion',
#         'nombre',
#         'link_relacionado',
#     ]
#     list_display_links = ['institucion', 'nombre',]
#     ordering = ['institucion', 'nombre',]
#     actions = [export_as_csv_action("Exportar Localidades Seleccionadas",)]
#     show_full_result_count = True
#     actions_selection_counter = True
#     list_select_related = True
#     inlines = [
#         # RequisitoIngresoInline,
#         # ServiciosInline,
#         TelefonoLocalidadInline,
#         CorreoLocalidadInline,
#         AyudaEconomicaLocalidadInline,
#         ActividadCulturalLocalidadInline,
#         DisciplinaDeportivaLocalidadInline,
#         OrganizacionEstudiantilLocalidadInline,
#         AgrupacionCivicaLocalidadInline,
#         RedSocialLocalidadInline,
#         SfcLocalidadInline,
#     ]

#     def link_relacionado(self, obj):
#         url = '../carrera/?id_localidad_pub__id_localidad__exact='
#         url_link = 'Ver Carreras en esta localidad'
#         return  mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_localidad, url_link))
#     link_relacionado.allow_tags = True
#     link_relacionado.short_description = 'Carreras en esta localidad'

#     def get_form(self, request, obj=None, **kwargs):

#         ModelForm = super(LocalidadAdmin, self).get_form(request, obj, **kwargs)

#         class ModelFormMetaClass(ModelForm):
#             def __new__(cls, *args, **kwargs):
#                 kwargs['request'] = request
#                 return ModelForm(*args, **kwargs)
#         return ModelFormMetaClass

#     def suit_row_attributes(self, obj):
#         css_class = {
#             '11011111': 'success', # Activo y públicado
#             '10011111': 'info', # Activo públicado en proceso de revisión
#             '00011111': 'warning', # Nuevo registro en revision sin publicar
#             '00001111': 'warning', # Nuevo registro inactivo en revision sin publicar
#         }.get(obj.cod_activacion)
#         if css_class == 'success':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'info':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'warning':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         else:
#             return {'class': 'error', 'data': obj.cod_activacion}

#     def save_model(self, request, obj, form, change):
#         if obj.publicar:
#             obj.editor = request.user.username
#         super(LocalidadAdmin, self).save_model(request, obj, form, change)


##############################################################################
@admin.register(AreaConocimiento)
class AreaConocimientoAdmin(admin.ModelAdmin):
    fields = [
        ('nombre_area_conocimiento',),
    ]
    search_fields = ['nombre_area_conocimiento', ]
    list_display = [
        'nombre_area_conocimiento',
        'link_relacionado',
    ]
    ordering = ['nombre_area_conocimiento', ]
    show_full_result_count = True
    actions_selection_counter = True
    list_select_related = True

    def link_relacionado(self, obj):
        url = '../subareaconocimiento/?q=&id_area_conocimiento__id_area_conocimiento__exact='
        url_link = 'Ver Sub Áreas de esta Área del Conocimiento'
        return  mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_area_conocimiento, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Sub Áreas de esta Área del Conocimiento'


##############################################################################
@admin.register(SubAreaConocimiento)
class SubAreaConocimientoAdmin(admin.ModelAdmin):
    fields = [
        ('id_area_conocimiento',),
        ('nombre_subarea_conocimiento',),
    ]

    search_fields = ['nombre_subarea_conocimiento',]

    list_filter = [
        ('id_area_conocimiento', admin.RelatedOnlyFieldListFilter),
    ]

    list_display = [
        'id_area_conocimiento',
        'nombre_subarea_conocimiento',
        'link_relacionado',
    ]

    list_display_links = [
        'id_area_conocimiento',
        'nombre_subarea_conocimiento',]

    ordering = ['id_area_conocimiento', 'nombre_subarea_conocimiento',]

    show_full_result_count = True

    actions_selection_counter = True

    list_select_related = True

    def link_relacionado(self, obj):
        url = '../carrera/?q=&id_sub_area_conocimiento_pub__id_sub_area_conocimiento__exact='
        url_link = 'Ver Programas de esta Sub Área del Conocimiento'
        return  mark_safe('<a href="%s%s">%s</a>' % (url, obj.id_sub_area_conocimiento, url_link))
    link_relacionado.allow_tags = True
    link_relacionado.short_description = 'Programas de esta Sub Área del Conocimiento'


# ##############################################################################
# class SfcCarreraInline(admin.TabularInline):
#     model = Carrera.sfc.through
#     extra = 1
#     verbose_name = "Soporte Formal de Cambio"
#     verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
# @admin.register(Carrera)
# class CarreraAdmin(admin.ModelAdmin):
#     search_fields = ['nombre', ]
#     fields = [
#         ('localidad', 'localidad_edit',),
#         ('tipo_carrera', 'id_tipo_carrera_edit',),
#         ('area_conocimiento', 'area_conocimiento_edit',),
#         ('subarea_conocimiento', 'sub_area_conocimiento_edit'),
#         ('campo_amplio', 'id_cine_f_campo_amplio_edit'),
#         ('campo_especifico', 'id_cine_f_campo_especifico_edit'),
#         ('campo_detallado', 'id_cine_f_campo_detallado_edit'),
#         ('titulo', 'id_titulo_edit'),
#         ('modalidad', 'id_modalidad_edit'),
#         ('duracion', 'duracion_edit'),
#         ('acreditadora', 'id_institucion_acreditadora_edit'),
#         ('nombre_carrera', 'nombre_carrera_edit'),
#         ('descripcion', 'descripcion_carrera_edit'),
#         ('mercado', 'mercado_ocupacional_edit'),
#         ('prioritaria', 'prioritaria_edit'),
#         ('usuario_revisor', 'revisor_edit'),
#         'usuario_editor',
#         'publicar',
#         'cod_activacion',
#     ]
#     form = CarreraForm
#     # search_fields = ['nombre', ]

#     list_filter = [
#         # ('id_localidad_pub', admin.RelatedOnlyFieldListFilter),
#         ('id_tipo_carrera_pub', admin.RelatedOnlyFieldListFilter),
#         ('id_sub_area_conocimiento_pub', admin.RelatedOnlyFieldListFilter),
#         ('id_titulo_pub', admin.RelatedOnlyFieldListFilter),
#         ('id_modalidad_pub', admin.RelatedOnlyFieldListFilter),
#         CodActCarrFilter,
#     ]
#     list_display = ['nombre', 'localidad',]
#     list_display_links = ['nombre', 'localidad',]
#     ordering = ['localidad', 'nombre',]
#     show_full_result_count = True
#     actions_selection_counter = True
#     list_select_related = True
#     inlines = [
#         SfcCarreraInline,
#     ]

#     def get_form(self, request, obj=None, **kwargs):

#         ModelForm = super(CarreraAdmin, self).get_form(
#             request, obj, **kwargs)

#         class ModelFormMetaClass(ModelForm):
#             def __new__(cls, *args, **kwargs):
#                 kwargs['request'] = request
#                 return ModelForm(*args, **kwargs)
#         return ModelFormMetaClass

#     def suit_row_attributes(self, obj):
#         css_class = {
#             '11111111': 'success', # Activo y públicado
#             '10111111': 'info', # Activo públicado en proceso de revisión
#             '00111111': 'warning', # Nuevo registro en revision sin publicar
#             '00011111': 'warning', # Nuevo registro inactivo en revision sin publicar
#         }.get(obj.cod_activacion)
#         if css_class == 'success':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'info':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         if css_class == 'warning':
#             return {'class': css_class, 'data': obj.cod_activacion}
#         else:
#             return {'class': 'error', 'data': obj.cod_activacion}

#     def save_model(self, request, obj, form, change):
#         if obj.publicar:
#             obj.editor = request.user.username
#         super(CarreraAdmin, self).save_model(request, obj, form, change)
