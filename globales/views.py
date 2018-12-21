# -*- coding: utf-8 -*-
"""
Vistas de la aplicación globales
"""
# Librerias Standard
import datetime
import urllib.request

# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import CreateView, UpdateView

# Librerias de terceros
from dal import autocomplete

# Librerias desarrolladas por mi
from globales.forms import InstitucionMinisterialForm
from globales.models import InstitucionMinisterial

# Librerias en carpetas locales
from .models import Estado, Etnia, Municipio, Pais, Parroquia, Saime


#@login_required
def index(request):
    return render(request, 'index.html')
##############################################################################
#          Vistas para la gestión del Modelo Instituciones Miniteriales      #
#                   Agregar e Actualizar los registros                       #
##############################################################################


##############################################################################
class AgregarInstitucionMinisterial(SuccessMessageMixin, CreateView):
    """Esta clase sirve para agregar las Instituciones Ministeriales
    """
    model = InstitucionMinisterial
    form_class = InstitucionMinisterialForm
    template_name = 'institucion_ministerial_formulario.html'
    success_url = reverse_lazy('globales:listar-institucion-ministerial')


##############################################################################
class EditarInstitucionMinisterial(SuccessMessageMixin, UpdateView):
    """Esta clase sirve para actualizar o editar las Instituciones Ministeriales
    almacenadas en la Base de Datos del modelo InstitucionMinisterial
    """
    model = InstitucionMinisterial
    form_class = InstitucionMinisterialForm
    template_name = 'institucion_ministerial_formulario.html'
    success_url = reverse_lazy('globales:listar-institucion-ministerial')


##############################################################################
class InstitucionIeuAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo TipoInstitucion
    """

    def get_queryset(self):
        queryset = InstitucionMinisterial.objects.filter(tipo_institucion='IEU')

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


##############################################################################
class PaisAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):


        if self.q:
            qs = Pais.objects.filter(
                nombrepais__istartswith=self.q).order_by('nombrepais')

        return qs


##############################################################################
class SaimeAutoComplete(autocomplete.Select2QuerySetView):
    """clase autocomplete especificamente del SAIME
    """
    def get_queryset(self):

        qs = Saime.objects.none()

        if self.q:
            qs = Saime.objects.filter(cedula_identidad=self.q)
        return qs


##############################################################################
class PersonaMujerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if self.q:
            qs = Saime.objects.filter(sexo='F', cedula_identidad=self.q)

        return qs


##############################################################################
class PersonaHombreAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
       
        if self.q:
            qs = Saime.objects.filter(sexo='M', cedula_identidad=self.q)

        return qs


##############################################################################
class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Saime.objects.none()

        sexo = self.forwarded.get('sexo', None)

        if self.q:
            if sexo == 'M':
                qs = Saime.objects.filter(sexo='F', cedula_identidad=self.q)
            elif sexo == 'F':
                qs = Saime.objects.filter(sexo='M', cedula_identidad=self.q)
            else:
                qs = Saime.objects.filter(cedula_identidad=self.q)

        return qs


##############################################################################
class PaisAutocomplete2(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if self.q:
            qs = Pais.objects.filter(
                nombrepais__istartswith=self.q).order_by('nombrepais')

        return qs


##############################################################################
class EstadoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Estado.objects.all()

        if self.q:
            qs = qs.filter(nombreestado__icontains=self.q).order_by('nombreestado')

        return qs


##############################################################################
class MunicipioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        estado = self.forwarded.get('estado_edit', None)
        if estado:
            qs = Municipio.objects.filter(idestadoglobal=estado)
        else:
            qs = Municipio.objects.all()

        if self.q:
            qs = qs.filter(nombremunicipio__icontains=self.q).order_by('nombremunicipio')

        return qs


##############################################################################
class ParroquiaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        municipio = self.forwarded.get('municipio_edit', None)
        if municipio:
            qs = Parroquia.objects.filter(idmunicipioglobal=municipio)
        else:
            qs = Parroquia.objects.all()

        if self.q:
            qs = qs.filter(nombreparroquia__icontains=self.q).order_by('nombreparroquia')

        return qs


##############################################################################
class EtniaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Etnia.objects.all()

        if self.q:
            qs = qs.filter(nombreetnia__istartswith=self.q)

        return qs




##############################################################################
