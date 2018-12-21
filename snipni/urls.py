from django.urls import path, reverse_lazy
from django.views.generic import DetailView, ListView

from oeuconfig.views import (
    AgregarModeloSimple, EditarModeloSimple,
    EliminarModeloSimple
)
from .models import SeguidorEstadal
from .forms import SeguidorEstadalForm
app_name= 'snipni'

urlpatterns = [
##############################################################################
###########               Seguidores Estadales                  ##############
# ############################################################################     
    path( # Listar
        'seguidor-estado',
        ListView.as_view(
            model=SeguidorEstadal,
            template_name='listar_seguidor.html',
            extra_context={'titulo': 'Seguidor Estadal'}
        ),
        name='listar-seguidor-estado'),
    path( # Detalle
        'seguidor-estado/detalle/<int:pk>',
        DetailView.as_view(
            model=SeguidorEstadal,
            template_name='detalle_seguidor.html',
            context_object_name='detalle',
            extra_context={'titulo':'Seguidor Estadal'}
        ),
        name='detalle-seguidor-estado'),
    path( # Agregar
        'seguidor-estado/agregar',
        AgregarModeloSimple.as_view(
            model=SeguidorEstadal,
            form_class=SeguidorEstadalForm,
            template_name='sni_formulario.html',
            success_url=reverse_lazy('snipni:listar-seguidor-estado'),
            success_message='¡El seguidor del estado se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo':'Seguidor Estadal'}
        ),
        name='agregar-seguidor-estado'),
    path( # Editar
        'seguidor-estado/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=SeguidorEstadal,
            form_class=SeguidorEstadalForm,
            template_name='formulario_sni.html',
            success_url=reverse_lazy('snipni:listar-seguidor-estado'),
            success_message='El seguidor del estado se actualizo' '\n'
                            'de manera exitosa!',
            extra_context={'titulo':'Seguidor Estadal'}
        ),
        name='editar-seguidor-estado'),
    path(  # Eliminar
        'seguidor-estado/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=SeguidorEstadal,
            template_name='eliminar_seguidor.html',
            success_url=reverse_lazy('snipni:listar-seguidor-estado'),
            relacion=None,
            relacion_id=None,
            success_message='¡El seguidor se eliminó de manera exitosa!',
            extra_context={'titulo': 'Seguidor Estadal'}
        ),
        name='eliminar-seguidor-estado'),

]