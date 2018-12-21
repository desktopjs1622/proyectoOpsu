# Librerias Django
from django.urls import path, reverse_lazy
from django.views.generic import DetailView, ListView

# Librerias de terceros
from oeuconfig.views import (
    AgregarModeloSimple, EditarModeloSimple, EliminarModeloSimple)

# Librerias en carpetas locales
from . import views
from sismeu.forms import ClinicaForm, RegionForm
from .models import (
    Departamento, TelefonoClinica, MotivoInactivacion, Convenios,
    HistoricoClinica, ConvenioClinica, Clinica, Region)
from .views import (
    EditarModelo, EstadoAutoComplete, MunicipioAutoComplete,
    ParroquiaAutocomplete, activar_clinica, contacto_clinica,
    desactivar_clinica, detalle_historia, detalles_clinica, eliminar_clinica,
    eliminar_region, formulario_clinica, index, lista_region,
    registro_region, eliminar_telefono, EstadoRegionAutoComplete, auditoria_clinica, detalle_auditoria)

from oeuconfig.views import AgregarModeloSimple, EditarModeloSimple, EliminarModeloSimple

app_name = 'sismeu'

urlpatterns = [
#############################################################################
#########                       index                             ###########
#############################################################################
    path(  # index
        '',
        index,
        name='index'),
#############################################################################
#########                       Clínica                            ##########
#############################################################################
    path(  # vista general de clinica
        'clinica',
        (views.lista_clinica),
        name = 'vista_general'),
    path(  # agregar Clinica
        'clinica/agregar',
        formulario_clinica,
        name='agregar_clinica'),
    path(  # Editar Clinica
        'clinica/editar/<int:id_clinica>',
        formulario_clinica,
        name='editar_clinica'),
    path(  # Detalles de las Clinicas
        'clinica/detalle/<int:id_clinica>',
        detalles_clinica,
        name='detalle_clinica'),
    path(  # Eliminar Clinica
        'clinica/eliminar/<int:id_clinica>',
        eliminar_clinica,
        name='eliminar_clinica'),
    path(  # Activar Clinica
        'clinica/activar/<int:id_clinica>',
        activar_clinica,
        name='activar_clinica'),
    path(  # Desactivar Clinica
        'clinica/desactivar/<int:id_clinica>',
        desactivar_clinica,
        name='desactivar_clinica'),
#############################################################################
#########                     Historico de la clínica              ##########
#############################################################################
    path(  # Historia de la clinica
        'clinica/historia/<int:historico_id>',
        detalle_historia,
        name='detalle_historia'),
#############################################################################
#########                          Región                          ##########
#############################################################################
    path(  # Lista de Regiones
        'region',
        lista_region,
        name="lista_region"),
    path(  # Agregar Región
        'region/agregar',
        registro_region,
        name='registro_region'),
    path(  # Editar Región
        'region/editar/<int:region_id>',
        registro_region,
        name='editar_region'),
    path(  # Eliminar Región
        'region/eliminar/<int:region_id>',
        eliminar_region,
        name="eliminar_region"),
#############################################################################
#########                  Telefonos de la clínica                 ##########
#############################################################################
    path( # Agregar Telefono
        'clinica/contacto/<int:id_clinica>',
        contacto_clinica,
        name='telefono_clinica',),
    path( # Editar telefono
        'clinica/contacto/editar/<int:id_clinica>/<int:telefono_id>',
        contacto_clinica,
        name="telefono-editar",),
    path( # Eliminar Telefono
        'clinica/contacto/<int:id_clinica>/<int:telefono_id>',
        eliminar_telefono,
        name='eliminar-telefono',),
##############################################################################
#########            Departamentos de la clínica                    ##########
##############################################################################

    path(  # Listar
        'departamento-clinica',
        ListView.as_view(
            model=Departamento,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Departamento de la Clínica'}
        ),
        name='listar-departamento-clinica'),
    path(  # Detalle
        'departamento-clinica/detalle/<int:pk>',
        DetailView.as_view(
            model=Departamento,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Departamento de la Clínica'}
        ),
        name='detalle-departamento-clinica'),
    path(  # Agregar
        'departamento-clinica/agregar',
        AgregarModeloSimple.as_view(
            model=Departamento,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('sismeu:listar-departamento-clinica'),
            success_message='¡El departamento se agregó de manera exitosa!',
            extra_context={'titulo': 'Departamento de la Clínica'}
        ),
        name='agregar-departamento-clinica'),
    path(  # Editar
        'departamento-clinica/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=Departamento,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('sismeu:listar-departamento-clinica'),
            success_message='¡El departamento se actualizó de manera exitosa!',
            extra_context={'titulo': 'Departamento de la Clínica'}
        ),
        name='editar-departamento-clinica'),
    path(  # Eliminar
        'departamento-clinica/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=Departamento,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('sismeu:listar-departamento-clinica'),
            relacion=TelefonoClinica,
            relacion_id='tipo_contacto',
            success_message='¡El departamento se eliminó de manera exitosa!',
            extra_context={'titulo': 'Departamento de la Clínica'}
        ),
        name='eliminar-motivo'),

##############################################################################
#########               Motivos de inactivación                     ##########
##############################################################################

    path(  # Listar
        'motivo-inactivacion',
        ListView.as_view(
            model=MotivoInactivacion,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Motivo de Inactivación'}
        ),
        name='listar-motivo-clinica'),
    path(  # Detalle
        'motivo-inactivacion/detalle/<int:pk>',
        DetailView.as_view(
            model=MotivoInactivacion,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Motivo de Inactivación'}
        ),
        name='detalle-motivo-clinica'),
    path(  # Agregar
        'motivo-inactivacion/agregar',
        AgregarModeloSimple.as_view(
            model=MotivoInactivacion,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('sismeu:listar-motivo-clinica'),
            success_message='¡El motivo se agregó de manera exitosa!',
            extra_context={'titulo': 'Motivo de Inactivación'}
        ),
        name='agregar-motivo-clinica'),
    path(  # Editar
        'motivo-inactivacion/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=MotivoInactivacion,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('sismeu:listar-motivo-clinica'),
            success_message='¡El motivo se actualizó de manera exitosa!',
            extra_context={'titulo': 'Motivo de Inactivación'}
        ),
        name='editar-motivo-clinica'),
    path(  # Eliminar
        'motivo-inactivacion/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=MotivoInactivacion,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('sismeu:listar-motivo-clinica'),
            relacion=HistoricoClinica,
            relacion_id='motivo_inactivacion_id',
            success_message='¡El motivo se eliminó de manera exitosa!',
            extra_context={'titulo': 'Motivo de Inactivación'}
        ),
        name='eliminar-motivo'),

##############################################################################
#########              Convenios de la clinica                      ##########
##############################################################################

    path(  # Listar
        'convenio-clinica',
        ListView.as_view(
            model=Convenios,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Convenio de la Clínica'}
        ),
        name='listar-convenio-clinica'),
    path(  # Detalle
        'convenio-clinica/detalle/<int:pk>',
        DetailView.as_view(
            model=Convenios,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Convenio de la Clínica'}
        ),
        name='detalle-convenio-clinica'),
    path(  # Agregar
        'convenio-clinica/agregar',
        AgregarModeloSimple.as_view(
            model=Convenios,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('sismeu:listar-convenio-clinica'),
            success_message='¡El convenio se agregó de manera exitosa!',
            extra_context={'titulo': 'Convenio de la Clínica'}
        ),
        name='agregar-convenio-clinica'),
    path(  # Editar
        'convenio-clinica/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=Convenios,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('sismeu:listar-convenio-clinica'),
            success_message='¡El convenio se actualizó de manera exitosa!',
            extra_context={'titulo': 'Convenio de la Clínica'}
        ),
        name='editar-convenio-clinica'),
    path(  # Eliminar
        'convenio-clinica/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=Convenios,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('sismeu:listar-convenio-clinica'),
            relacion=ConvenioClinica,
            relacion_id='convenio',
            success_message='¡El convenio se eliminó de manera exitosa!',
            extra_context={'titulo': 'Convenio de la Clínica'}
        ),
        name='eliminar-convenio'),

##############################################################################
#########                       Auditoria                          ###########
##############################################################################
    path(  # vista general de clinica
        'auditoria',
        (views.auditoria_clinica),
        name = 'lista-auditoria'),
    path(  # vista general de clinica
        'auditoria/detalle/<int:auditoria_id>',
        (views.detalle_auditoria),
        name = 'detalle-auditoria'),
##############################################################################
#########                   AutoComplete                            ##########
##############################################################################
    path( # Estado de las regiones
        'EstadoRegionAutoComplete/',
        (views.EstadoRegionAutoComplete.as_view()),
        name='EstadoRegionAutoComplete'),
    path( # Estado
        'EstadoAutoComplete/',
        (views.EstadoAutoComplete.as_view()),
        name='EstadoAutoComplete'),
    path( # Municipio
        'MunicipioAutoComplete/',
        (views.MunicipioAutoComplete.as_view()),
        name='MunicipioAutoComplete'),
    path( # Parroquia
        'ParroquiaAutoComplete/',
        (views.ParroquiaAutocomplete.as_view()),
        name='ParroquiaAutoComplete'),
]
