"""
    Definición de las URI's para la aplicación globales
"""
# Librerias Django
from django.contrib.auth.decorators import permission_required
from django.urls import path, reverse_lazy
from django.views.generic import DetailView, ListView

# Librerias de terceros
from oeuconfig.views import (
    AgregarModeloSimple, EditarModeloSimple, EliminarModeloSimple)

# Librerias desarrolladas por mi
from globales.models import InstitucionMinisterial
from globales.views import *

# Librerias en carpetas locales
from . import views

app_name = 'globales'

urlpatterns = [
    ##########################################################################
    path( # Autocomletado para las Instituciones ministeriales que son IEU
        'institucion-ministerial-ieu/',
        InstitucionIeuAutoComplete.as_view(),
        name='institucion-ministerial-ieu'
    ),

    path('', views.index, name='index'),
    
    path('personaAutoComplete/',
        permission_required('demografia.ctrl_comunidad')(
            views.PersonaAutocomplete.as_view()),
        name='personaAutoComplete',
    ),
    path('personaHombreAutoComplete/',
        permission_required('demografia.ctrl_comunidad')(
            views.PersonaHombreAutocomplete.as_view()),
        name='hombreAutoComplete'
    ),
    path('personaMujerAutoComplete/',
        permission_required('demografia.ctrl_comunidad')(
            views.PersonaMujerAutocomplete.as_view()),
        name='mujerAutoComplete'
    ),
    path('paisAutoComplete/',
        permission_required('demografia.ctrl_comunidad')(
            views.PaisAutocomplete.as_view()),
        name='paisAutoComplete'
    ),
    path('paisAutoComplete2/',
        permission_required('demografia.ctrl_comunidad')(
            views.PaisAutocomplete2.as_view()),
        name='paisAutoComplete2'
    ),
    path('etniaAutoComplete/',
        permission_required('demografia.ctrl_comunidad')(
            views.EtniaAutocomplete.as_view()),
        name='etniaAutoComplete'
    ),
    path('estadoAutoComplete/', 
        EstadoAutocomplete.as_view(), 
        name='estadoAutoComplete'
    ),
    path('municipioAutoComplete/', 
        MunicipioAutocomplete.as_view(), 
        name='municipioAutoComplete'
    ),
    path('parroquiaAutoComplete/', 
        ParroquiaAutocomplete.as_view(), 
        name='parroquiaAutoComplete'
    ),


    ###################### Instituciones Ministeriales #######################
    path(  # Listar
        'institucion-ministerial',
        ListView.as_view(
            model=InstitucionMinisterial,
            template_name='institucion_ministerial_listar.html',
            extra_context={'titulo': 'Institución Ministerial'}
        ),
        name='listar-institucion-ministerial'),
    path(  # Detalle
        'institucion-ministerial/detalle/<int:pk>',
        DetailView.as_view(
            model=InstitucionMinisterial,
            template_name='institucion_ministerial_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Institución Ministerial'}
        ),
        name='detalle-institucion-ministerial'),
    path(  # Agregar
        'institucion-ministerial/agregar',
        AgregarInstitucionMinisterial.as_view(
            success_message='¡La institución Ministerial se agregó de manera exitosa!',
            extra_context={'titulo': 'Institución Ministerial'}
        ),
        name='agregar-institucion-ministerial'),
    path(  # Editar
        'institucion-ministerial/editar/<int:pk>',
        EditarInstitucionMinisterial.as_view(
            model=InstitucionMinisterial,
            success_message='¡La institución Ministerial se actualizó de manera exitosa!',
            extra_context={'titulo': 'Institución Ministerial'}
        ),
        name='editar-institucion-ministerial'),
    path(  # Eliminar
        'institucion-ministerial/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=InstitucionMinisterial,
            template_name='institucion_ministerial_eliminar.html',
            success_url=reverse_lazy('globales:listar-institucion-ministerial'),
            success_message='¡La institución Ministerial se eliminó de manera exitosa!',
            extra_context={'titulo': 'Institución Ministerial'}
        ),
        name='eliminar-institucion-ministerial'),


    ########################### AutoComplete Saime ###########################
    path(
        'saimeAutocomplete/',
        SaimeAutoComplete.as_view(),
        name='autocompleteSaime',
    ),


]
