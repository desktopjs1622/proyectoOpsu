"""Actos de grado URL Configuration
"""
# Librerias Django
from django.contrib.auth.decorators import permission_required
from django.urls import path, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

# Librerias en carpetas locales
from .forms import ActogradoForm
from .metodos import date
from .models import Actogrado, Graduando
from .views2 import *

app_name = 'grado'

urlpatterns = [

    path('',
    permission_required('grado.admin_grado')(ListarActo.as_view()),
        name = 'act_list'),
    
    path('create/',
    permission_required('grado.admin_grado')(GenerarActo.as_view()),
        name = 'act_generate'),
    
    path('edit_acto/<int:pk>/',
    permission_required('grado.admin_grado')(EditarActo.as_view()),
        name = 'act_edit'),

    path('cerrar_acto/acta-<int:pk>/',
    permission_required('grado.admin_grado')(CerrarActo.as_view()),
        name = 'act_close'),
    

    path('detalle_acto/<int:pk>',
    permission_required('grado.admin_grado')(CerrarActo.as_view(
        template_name = 'actos/detail.html',
        model = Actogrado,
        extra_context = {'titulo':'Acto de grado con acta nro. ',
        'label':'check',
        'tag':'primary',}
    )),
        name = 'act_detail'),

    path('eliminar_acto/<int:pk>/',
    permission_required('grado.admin_grado')(EliminarActo.as_view()),
        name = 'act_delete'),

    ###############################################################

    path('graduando/<int:pk>/list',
    permission_required('grado.admin_grado')(ListGraduando.as_view()),
        name = 'grad_list'),

    path('graduando/<int:pk>/',
    permission_required('grado.admin_grado')(DetailView.as_view(
        model = Graduando,
        template_name = 'graduandos/modal_detalle_graduando.html',
        extra_context = {'titulo':'Graduando'}
    )),
        name = 'grad_detail'),
    
    path('graduando/create/<int:pk>',
    permission_required('grado.admin_grado')(CreateGraduando.as_view()),
        name = 'grad_create'),


    path('graduando/edit/<int:pk>/<int:acto>/',
    permission_required('grado.admin_grado')(UpdateGraduando.as_view()),
        name = 'grad_edit'),

    path('graduando/delete/<int:pk>/<int:acto>',
    permission_required('grado.admin_grado')(DeleteGraduando.as_view()),
        name = 'grad_delete'),

    path('autocomplete_persona/',
    permission_required('grado.admin_grado')(PersonaAutocomplete.as_view()),
        name = 'persona_autocomplete'),

]
