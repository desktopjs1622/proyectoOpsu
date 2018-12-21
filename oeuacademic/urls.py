
# Librerias Django
from django.urls import path, reverse_lazy
from django.views.generic import DetailView, ListView

#Vistas importadas de la app oeuconfig view.py
from oeuacademic.views import (
    AgregarSAC, AreaConocimientoAutoComplete, CineFCampoAmplioAutoComplete,
    CineFCampoDetalladoAutoComplete, CineFCampoEspecificoAutoComplete,
    EditarSAC, SubAreaConocimientoAutoComplete, LocalidadesAutoComplete,
    AcreditadoraAutoComplete)
from oeuconfig.views import (
    AgregarModeloSimple, EditarModeloSimple, EliminarModeloSimple)
from oeu.views import (
    AgregarModeloComplejo, EditarModeloComplejo, EliminarModeloComplejo,
    ListarModeloComplejo)

#formulario importado de las apps (oeu oeuacademic) forms.py
from oeuacademic.forms import CarreraPreGradoForm, CARRERA_FORMSET
from oeu.models import CarreraRevisorEdit
from oeu.forms import TIPOIEUSFC_FORMSET

#Modelo importado de la app oeu models.py
from oeu.models import AreaConocimiento, Carrera, SubAreaConocimiento
#Vista importadas de la app oeu view.py
from oeu.views import ListarModeloComplejo

app_name = 'oeuacademic'

urlpatterns = [
    # ############### rutas para las areas de conocimientos ##################
    path(  # Listar
        'area-de-conocimiento/',
        ListarModeloComplejo.as_view(
            model=AreaConocimiento,
            template_name='area_conocimiento_listar.html',
            extra_context={'titulo': 'Áreas de Conocimientos'},
            filtro_por='id'
        ),
        name='listar-area-de-conocimiento'),
    path(  # Detalle
        'area-de-conocimiento/detalle/<int:pk>',
        DetailView.as_view(
            model=AreaConocimiento,
            template_name='area_conocimiento_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Áreas de Conocimientos'}
        ),
        name='detalle-area-de-conocimiento'),
    path(  # Agregar
        'area-de-conocimiento/agregar',
        AgregarModeloSimple.as_view(
            model=AreaConocimiento,
            fields=['nombre_area_conocimiento', 'descripcion'],
            template_name='area_conocimiento_formulario.html',
            success_url=reverse_lazy('oeuacademic:listar-area-de-conocimiento'),
            success_message='¡El área de conocimiento se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Áreas de Conocimientos'}
        ),
        name='agregar-area-de-conocimiento'),
    path(  # Editar
        'area-de-conocimiento/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=AreaConocimiento,
            fields=['nombre_area_conocimiento', 'descripcion'],
            template_name='area_conocimiento_formulario.html',
            success_url=reverse_lazy('oeuacademic:listar-area-de-conocimiento'),
            success_message='¡El área de conocimiento  se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Áreas de Conocimientos'}
        ),
        name='editar-area-de-conocimiento'),
     path(  # Eliminar
        'area-de-conocimiento/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=AreaConocimiento,
            template_name='area_conocimiento_eliminar.html',
            success_url=reverse_lazy('oeuacademic:listar-area-de-conocimiento'),
            relacion=SubAreaConocimiento,
            relacion_id='id_area_conocimiento',
            success_message='¡El área de conocimiento se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Áreas de Conocimientos'}
        ),
        name='eliminar-area-conocimiento'),


    # ############### rutas para las sub areas de conocimientos ################
    path(  # Listar
        'sub-area-de-conocimiento/',
        ListarModeloComplejo.as_view(
            model=SubAreaConocimiento,
            template_name='sub_area_conocimiento_listar.html',
            extra_context={'titulo': 'Sub áreas de Conocimientos'},
            filtro_por='id_area_conocimiento'
        ),
        name='listar-sub-area-de-conocimiento'),
    path(  # Detalle
        'sub-area-de-conocimiento/detalle/<int:pk>',
        DetailView.as_view(
            model=SubAreaConocimiento,
            template_name='sub_area_conocimiento_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Sub áreas de Conocimientos'}
        ),
        name='detalle-sub-area-de-conocimiento'),
    path(  # Agregar
        'sub-area-de-conocimiento/agregar',
        AgregarSAC.as_view(
            success_message='¡La Sub Área de Conocimiento se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Sub áreas de Conocimientos'}
        ),
        name='agregar-sub-area-de-conocimiento'),
     path(  # Editar
        'sub-area-de-conocimiento/editar/<int:pk>',
        EditarSAC.as_view(
            success_message='¡La Sub Área de Conocimiento se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Sub áreas de Conocimientos'}
        ),
        name='editar-sub-area-de-conocimiento'),
    path(  # Eliminar
        'sub-area-de-conocimiento/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=SubAreaConocimiento,
            template_name='sub_area_conocimiento_eliminar.html',
            success_url=reverse_lazy(
                'oeuacademic:listar-sub-area-de-conocimiento'),
            success_message='¡La sub área de conocimiento se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Sub áreas de Conocimientos'}
        ),
        name='eliminar-sub-area-conocimiento'),


##############################################################################
#########          Clase del autocomplete para Area y Sub-Area      ##########
#########                            Conocimientos                  ##########
##############################################################################
    path( #AutoComplete SubAreaConocimiento
        'SACAutocomplete',
        SubAreaConocimientoAutoComplete.as_view(),
        name='sub-area-conocimiento'),

    path( # AutoComplete AreaConocimiento
        'ACAutocomplete',
        AreaConocimientoAutoComplete.as_view(),
        name='area-conocimiento'),


##############################################################################
#########          Clase del autocomplete para cine_f_campo         ##########
#########               amplio, especifico y detallado              ##########
##############################################################################

    path( # Cine_f_campo_amplio
        'CFCAmplio',
        CineFCampoAmplioAutoComplete.as_view(),
        name='cine-f-campo-amplio'),

    path( #Cine_f_campo_especifico
        'CFCEspecifico',
        CineFCampoEspecificoAutoComplete.as_view(),
        name='cine-f-campo-especifico'),
    
    path( #Cine_f_campo_detallado
        'CFCDetallado',
        CineFCampoDetalladoAutoComplete.as_view(),
        name='cine-f-campo-detallado'),


##############################################################################
#########          Clase del autocomplete para Localidades          ##########
##############################################################################
    path( # Localidades
        'Localidad',
        LocalidadesAutoComplete.as_view(),
        name='localidades'),


##############################################################################
#########       Clase del autocomplete para IEU Acreditadora        ##########
##############################################################################
    path(#Institución Acreditadora
        'Acreditadora',
        AcreditadoraAutoComplete.as_view(),
        name='acreditadora'),


    # #################### Carreras Universitarias ######################### #
    path(  # Listar
        'pre-grado',
        ListarModeloComplejo.as_view(
            model=Carrera,
            template_name='carrera_pre_listar.html',
            filtro_por='localidad',
            extra_context={'titulo': 'Carreras de Pre-grado'}
        ),
        name='listar-carrera-pre'),
    path(  # Detalle
        'pre-grado/detalle/<int:pk>',
        DetailView.as_view(
            model=Carrera,
            template_name='carrera_pre_detalle.html',
            extra_context={'titulo': 'Carreras de Pre-grado'}
        ),
        name='detalle-carrera-pre-grado'),
     path(  # Agregar
        'pre-grado/agregar',
        AgregarModeloComplejo.as_view(
            model=Carrera,
            form_class=CarreraPreGradoForm,
            success_url=reverse_lazy('oeuacademic:listar-carrera-pre'),
            template_name='carrera_pre_formulario.html',
            extra_context={'titulo': 'Carreras de Pre-grado'},
            success_message='¡El tipo de Carrera se agregó' '\n'
                            'de manera exitosa!',
            posicion=7,
            revisor_edit=CarreraRevisorEdit,
            SfcFormSet=CARRERA_FORMSET
        ),
        name='agregar-carrera-pre-grado'),
    path(  # Editar
        'pre-grado/editar/<int:pk>',
        EditarModeloComplejo.as_view(
            model=Carrera,
            form_class=CarreraPreGradoForm,
            success_url=reverse_lazy('oeuacademic:listar-carrera-pre'),
            template_name='carrera_pre_formulario.html',
            extra_context={'titulo': 'Carreras de Pre-grado'},
            success_message='¡El tipo de Carrera se actualizó' '\n'
                        'de manera exitosa!',
            posicion=7,
            revisor_edit=CarreraRevisorEdit,
            relacion_id='carrera_pre_id',
            SfcFormSet=CARRERA_FORMSET
        ),
        name='editar-carrera-pre-grado'),
    path(  # Eliminar
        'pre-grado/eliminar/<int:pk>',
        EliminarModeloComplejo.as_view(
            model=Carrera,
            template_name='carrera_pre_eliminar.html',
            success_url=reverse_lazy('oeuacademic:listar-carrera-pre'),
            extra_context={'titulo': 'Carreras de Pre-grado'},
        ),
        name='eliminar-carrera-pre-grado'),


# ################################################################################# #
    #  path(  # Listar
    #     'sub-tipo-carreras-universitarias',
    #     ListarModeloComplejo.as_view(
    #         model = Carrera,
    #         template_name='sub_tipo_carrera_universitaria_listar.html',
    #         extra_context={'titulo': 'Sub Tipos de Carreras Universitarias'}
    #     ),
    #     name='listar-sub-tipo-carreras-universitarias'),
]
