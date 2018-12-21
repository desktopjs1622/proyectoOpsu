"""Ruta para la aplicación del Libro de Oportunidades de Estudio Universitaria
"""
# Librerias Django
from django.urls import path, reverse_lazy
from django.views.generic import DetailView

# Librerias desarrolladas por mi
from oeu.forms import (
    IEUSFC_FORMSET, LOCALIDADSFC_FORMSET, SUBTIPOIEUSFC_FORMSET,
    TIPOESPECIFICOIEUSFC_FORMSET, TIPOIEUSFC_FORMSET, IeuForm, LocalidadForm,
    SubTipoIeuForm, TipoEspecificoIeuForm, TipoIeuForm)
from oeu.models import (
    Carrera, Ieu, IeuRevisorEdit, IeuSfc, Localidad, LocalidadRevisorEdit,
    LocalidadSfc, SubTipoInstitucion, SubTipoInstitucionRevisorEdit,
    SubTipoInstitucionSfc, TipoEspecificoIeuRevisorEdit, TipoEspecificoIeuSfc,
    TipoEspecificoInstitucion, TipoInstitucion, TipoInstitucionRevisorEdit,
    TipoInstitucionSfc)
from oeu.views import (
    AgregarModeloComplejo, AreaAutocomplete, CarreraAutocomplete,
    EditarModeloComplejo, EliminarModeloComplejo, IeuAutocomplete,
    ListarModeloComplejo, LocalidadIeuAutocomplete, SubAreaAutocomplete,
    SubTipoIeuAutoComplete, TipoEspecificoIeuAutocomplete, TipoIeuAutoComplete)

app_name = 'oeu'

urlpatterns = [
    # #################### Servicios de auto completado #################### #
    path('tipo-ieu-au/', TipoIeuAutoComplete.as_view(), name='tipo-ieu-au'),
    path(
        'sub-tipo-ieu-au/',
        SubTipoIeuAutoComplete.as_view(),
        name='sub-tipo-ieu-au'
    ),
    path(
        'tipo-especifico-ieu/',
        TipoEspecificoIeuAutocomplete.as_view(),
        name='tipo-especifico-ieu',
    ),
    path(
        'ieu/',
        IeuAutocomplete.as_view(),
        name='ieu',
    ),
    path(
        'localidad-ieu/',
        LocalidadIeuAutocomplete.as_view(),
        name='localidad-ieu'),
    path('area', AreaAutocomplete.as_view(), name='area'),
    path('subarea', SubAreaAutocomplete.as_view(), name='subarea'),
    path('carrera', CarreraAutocomplete.as_view(), name='carrera'),


    # ##################### rutas para los tipos de ieu #################### #
    path(  # Listar
        'instituciones/tipo-ieu',
        ListarModeloComplejo.as_view(
            model=TipoInstitucion,
            template_name='tipo_ieu_listar.html',
            filtro_por='id'
        ),
        name='listar-tipo-ieu'),
    path(  # Detalle
        'instituciones/tipo-ieu/detalle/<int:pk>',
        DetailView.as_view(
            model=TipoInstitucion,
            template_name='tipo_ieu_detalle.html'
        ),
        name='detalle-tipo-ieu'),
    path(  # Agregar
        'instituciones/tipo-ieu/agregar',
        AgregarModeloComplejo.as_view(
            model=TipoInstitucion,
            form_class=TipoIeuForm,
            success_url=reverse_lazy('oeu:listar-tipo-ieu'),
            template_name='tipo_ieu_formulario.html',
            posicion=7,
            revisor_edit=TipoInstitucionRevisorEdit,
            success_message='¡El tipo de IEU se agregó' '\n'
                            'de manera exitosa!',
            SfcFormSet=TIPOIEUSFC_FORMSET
        ),
        name='agregar-tipo-ieu'),
    path(  # Editar
        'instituciones/tipo-ieu/editar/<int:pk>',
        EditarModeloComplejo.as_view(
            model=TipoInstitucion,
            form_class=TipoIeuForm,
            success_url=reverse_lazy('oeu:listar-tipo-ieu'),
            template_name='tipo_ieu_formulario.html',
            posicion=7,
            revisor_edit=TipoInstitucionRevisorEdit,
            relacion_id='tipo_ieu_id',
            success_message='¡El tipo de IEU se actualizó' '\n'
                            'de manera exitosa!',
            SfcFormSet=TIPOIEUSFC_FORMSET
        ),
        name='editar-tipo-ieu'),
    path(  # Eliminar
        'instituciones/tipo-ieu/eliminar/<int:pk>',
        EliminarModeloComplejo.as_view(
            model=TipoInstitucion,
            template_name='tipo_ieu_eliminar.html',
            success_url=reverse_lazy('oeu:listar-tipo-ieu'),
            relacion=SubTipoInstitucion,
            relacion_id='tipo_ieu',
            rel_sfc=TipoInstitucionSfc,
        ),
        name='eliminar-tipo-ieu'),


    # ################### rutas par los sub tipos de ieu ################### #
    path(  # Listar
        'instituciones/sub-tipo-ieu/',
        ListarModeloComplejo.as_view(
            model=SubTipoInstitucion,
            template_name='sub_tipo_ieu_listar.html',
            filtro_por='tipo_ieu_id'
        ),
        name='listar-sub-tipo-ieu'),
    path(  # Detalle
        'instituciones/sub-tipo-ieu/detalle/<int:pk>',
        DetailView.as_view(
            model=SubTipoInstitucion,
            template_name='sub_tipo_ieu_detalle.html'
        ),
        name='detalle-sub-tipo-ieu'),
    path(  # Agregar
        'instituciones/sub-tipo-ieu/agregar',
        AgregarModeloComplejo.as_view(
            model=SubTipoInstitucion,
            form_class=SubTipoIeuForm,
            success_url=reverse_lazy('oeu:listar-sub-tipo-ieu'),
            template_name='sub_tipo_ieu_formulario.html',
            posicion=6,
            revisor_edit=SubTipoInstitucionRevisorEdit,
            success_message='¡El sub tipo de IEU se agregó' '\n'
                            'de manera exitosa!',
            SfcFormSet=SUBTIPOIEUSFC_FORMSET
        ),
        name='agregar-sub-tipo-ieu'),
    path(  # Editar
        'instituciones/sub-tipo-ieu/editar/<int:pk>',
        EditarModeloComplejo.as_view(
            model=SubTipoInstitucion,
            form_class=SubTipoIeuForm,
            success_url=reverse_lazy('oeu:listar-sub-tipo-ieu'),
            template_name='sub_tipo_ieu_formulario.html',
            posicion=6,
            revisor_edit=SubTipoInstitucionRevisorEdit,
            relacion_id='sub_tipo_ieu_id',
            success_message='¡El sub tipo de IEU se editó' '\n'
                            'de manera exitosa!',
            SfcFormSet=SUBTIPOIEUSFC_FORMSET
        ),
        name='editar-sub-tipo-ieu'),
    path(  # Eliminar
        'instituciones/sub-tipo-ieu/eliminar/<int:pk>',
        EliminarModeloComplejo.as_view(
            model=SubTipoInstitucion,
            template_name='sub_tipo_ieu_eliminar.html',
            success_url=reverse_lazy('oeu:listar-sub-tipo-ieu'),
            relacion=TipoEspecificoInstitucion,
            relacion_id='sub_tipo_ieu',
            rel_sfc=SubTipoInstitucionSfc,
        ),
        name='eliminar-sub-tipo-ieu'),


    # ############### rutas par los tipos especificos de ieu ############### #
    path(  # Listar
        'instituciones/tipo-especifico-ieu/',
        ListarModeloComplejo.as_view(
            model=TipoEspecificoInstitucion,
            template_name='tipo_especifico_ieu_listar.html',
            filtro_por='sub_tipo_ieu_id'
        ),
        name='listar-tipo-especifico-ieu'),
    path(  # Detalle
        'instituciones/tipo-especifico-ieu/detalle/<int:pk>',
        DetailView.as_view(
            model=TipoEspecificoInstitucion,
            template_name='tipo_especifico_ieu_detalle.html'
        ),
        name='detalle-tipo-especifico-ieu'),
    path(  # Agregar
        'instituciones/tipo-especifico-ieu/agregar',
        AgregarModeloComplejo.as_view(
            model=TipoEspecificoInstitucion,
            form_class=TipoEspecificoIeuForm,
            relacion_id='tipo_especifico_ieu',
            success_url=reverse_lazy('oeu:listar-tipo-especifico-ieu'),
            template_name='tipo_especifico_ieu_formulario.html',
            posicion=5,
            revisor_edit=TipoEspecificoIeuRevisorEdit,
            success_message='¡El tipo de IEU especíco se agregó de manera \
            exitosa!',
            SfcFormSet=TIPOESPECIFICOIEUSFC_FORMSET
        ),
        name='agregar-tipo-especifico-ieu'),
    path(  # Editar
        'instituciones/tipo-especifico-ieu/editar/<int:pk>',
        EditarModeloComplejo.as_view(
            model=TipoEspecificoInstitucion,
            form_class=TipoEspecificoIeuForm,
            relacion_id='tipo_especifico_ieu',
            success_url=reverse_lazy('oeu:listar-tipo-especifico-ieu'),
            template_name='tipo_especifico_ieu_formulario.html',
            posicion=5,
            revisor_edit=TipoEspecificoIeuRevisorEdit,
            success_message='¡El tipo de IEU especíco se editó de manera \
            exitosa!',
            SfcFormSet=TIPOESPECIFICOIEUSFC_FORMSET
        ),
        name='editar-tipo-especifico-ieu'),
    path(  # Eliminar
        'instituciones/tipo-especifico-ieu/eliminar/<int:pk>',
        EliminarModeloComplejo.as_view(
            model=TipoEspecificoInstitucion,
            template_name='tipo_especifico_ieu_eliminar.html',
            success_url=reverse_lazy('oeu:listar-tipo-especifico-ieu'),
            relacion=Ieu,
            relacion_id='tipo_especifico_ieu',
            rel_sfc=TipoEspecificoIeuSfc,
        ),
        name='eliminar-tipo-especifico-ieu'),


    # ######################### rutas par las ieu ########################## #
    path(  # Listar
        'instituciones/ieu/',
        ListarModeloComplejo.as_view(
            model=Ieu,
            template_name='ieu_listar.html',
            filtro_por='tipo_especifico_ieu_id'
        ),
        name='listar-ieu'),
    path(  # Detalle
        'instituciones/ieu/detalle/<int:pk>',
        DetailView.as_view(
            model=Ieu,
            template_name='ieu_detalle.html'
        ),
        name='detalle-ieu'),
    path(  # Agregar
        'instituciones/ieu/agregar',
        AgregarModeloComplejo.as_view(
            model=Ieu,
            form_class=IeuForm,
            relacion_id='ieu',
            success_url=reverse_lazy('oeu:listar-ieu'),
            template_name='ieu_formulario.html',
            posicion=4,
            revisor_edit=IeuRevisorEdit,
            success_message='¡La IEU se agregó de manera exitosa!',
            SfcFormSet=IEUSFC_FORMSET
        ),
        name='agregar-ieu'),
    path(  # Editar
        'instituciones/ieu/editar/<int:pk>',
        EditarModeloComplejo.as_view(
            model=Ieu,
            form_class=IeuForm,
            relacion_id='ieu',
            success_url=reverse_lazy('oeu:listar-ieu'),
            template_name='ieu_formulario.html',
            posicion=4,
            revisor_edit=IeuRevisorEdit,
            success_message='¡La IEU se editó de manera exitosa!',
            SfcFormSet=IEUSFC_FORMSET
        ),
        name='editar-ieu'),
    path(  # Eliminar
        'instituciones/ieu/eliminar/<int:pk>',
        EliminarModeloComplejo.as_view(
            model=Ieu,
            template_name='ieu_eliminar.html',
            success_url=reverse_lazy('oeu:listar-ieu'),
            relacion=Localidad,
            relacion_id='ieu',
            rel_sfc=IeuSfc,
        ),
        name='eliminar-ieu'),


    # ##################### rutas par las localidades ###################### #
    path(  # Listar
        'instituciones/localidad/',
        ListarModeloComplejo.as_view(
            model=Localidad,
            template_name='localidad_listar.html',
            filtro_por='ieu_id'
        ),
        name='listar-localidad'),
    path(  # Detalle
        'instituciones/localidad/detalle/<int:pk>',
        DetailView.as_view(
            model=Localidad,
            template_name='localidad_detalle.html'
        ),
        name='detalle-localidad'),
    path(  # Agregar
        'instituciones/localidad/agregar',
        AgregarModeloComplejo.as_view(
            model=Localidad,
            form_class=LocalidadForm,
            relacion_id='localidad',
            success_url=reverse_lazy('oeu:listar-localidad'),
            template_name='localidad_formulario.html',
            posicion=3,
            revisor_edit=LocalidadRevisorEdit,
            success_message='¡La Localidad se agregó de manera exitosa!',
            SfcFormSet=LOCALIDADSFC_FORMSET
        ),
        name='agregar-localidad'),
    path(  # Editar
        'instituciones/localidad/editar/<int:pk>',
        EditarModeloComplejo.as_view(
            model=Localidad,
            form_class=LocalidadForm,
            relacion_id='localidad',
            success_url=reverse_lazy('oeu:listar-localidad'),
            template_name='localidad_formulario.html',
            posicion=3,
            revisor_edit=LocalidadRevisorEdit,
            success_message='¡La Localidad se editó de manera exitosa!',
            SfcFormSet=LOCALIDADSFC_FORMSET
        ),
        name='editar-localidad'),
    path(  # Eliminar
        'instituciones/localidad/eliminar/<int:pk>',
        EliminarModeloComplejo.as_view(
            model=Localidad,
            template_name='localidad_eliminar.html',
            success_url=reverse_lazy('oeu:listar-localidad'),
            relacion=Carrera,
            relacion_id='localidad',
            rel_sfc=LocalidadSfc,
        ),
        name='eliminar-localidad'),
]
