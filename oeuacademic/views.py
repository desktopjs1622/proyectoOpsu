# Librerias Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

# Librerias de terceros
from dal import autocomplete
from oeuacademic.forms import SubAreaConocimientoForm
from oeuconfig.models import SoporteFormalCambio

# Librerias desarrolladas por mi
from oeu.models import (
    AreaConocimiento, CineFCampoAmplio, CineFCampoEspecifico,
    SubAreaConocimiento, CineFCampoDetallado, Localidad, Ieu)

##############################################################################
#          Vistas para la gestión de los modelos agregar y editar            #
#                    las sub areas de conocimientos                          #
##############################################################################


##############################################################################
class AgregarSAC(SuccessMessageMixin, CreateView):
    """Con esta clase se puede agregar las sub áreas de conocimientos.
    """
    model = SubAreaConocimiento
    form_class = SubAreaConocimientoForm
    template_name = 'sub_area_conocimiento_formulario.html'
    success_url = reverse_lazy('oeuacademic:listar-sub-area-de-conocimiento')


##############################################################################
class EditarSAC(SuccessMessageMixin, UpdateView):
    """Con esta clase se puede editar las sub áreas de conocimientos.
    """
    model = SubAreaConocimiento
    form_class = SubAreaConocimientoForm
    template_name = 'sub_area_conocimiento_formulario.html'
    success_url = reverse_lazy('oeuacademic:listar-sub-area-de-conocimiento')


##############################################################################
#########          Clase del autocomplete de areas y sub            ##########
#########                  areas de conocimientos                   ##########
##############################################################################
class AreaConocimientoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar las areas de conocimientos.
    """
    def get_queryset(self):
        queryset = AreaConocimiento.objects.all()

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


class SubAreaConocimientoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar las sub areas de conocimientos.
    """
    def get_queryset(self):
        area_conocimiento = self.forwarded.get('area_conocimiento_edit', None)

        queryset = SubAreaConocimiento.objects.all()

        if area_conocimiento:
            queryset = queryset.filter(id_area_conocimiento=area_conocimiento)
        
        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)
        
        return queryset


##############################################################################
#########          Clase del autocomplete para cine_f_campo         ##########
#########               amplio, especifico y detallado              ##########
##############################################################################

class CineFCampoAmplioAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar Cine_F_Campo_Amplio.
    """
    def get_queryset(self):
        queryset = CineFCampoAmplio.objects.all()

        if self.q:
            queryset = queryset.filter(descripcion_campo_amplio_icontains=self.q)

        return queryset


class CineFCampoEspecificoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar Cine_F_Campo_Especifico.
    """
    def get_queryset(self):
        cine_f_campo_amplio = self.forwarded.get('cine_f_campo_amplio_edit', None)

        queryset = CineFCampoEspecifico.objects.all()

        if cine_f_campo_amplio:
            queryset = queryset.filter(id_cine_f_campo_amplio=cine_f_campo_amplio)

        if self.q:
            queryset = queryset.filter(descripcion_campo_especifico_icontains=self.q)

        return queryset


class CineFCampoDetalladoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar Cine_F_Campo_Detallado.
    """
    def get_queryset(self):
        cine_f_campo_especifico = self.forwarded.get('cine_f_campo_especifico_edit', None)

        queryset = CineFCampoDetallado.objects.all()

        if cine_f_campo_especifico:
            queryset = queryset.filter(id_cine_f_campo_especifico=cine_f_campo_especifico)

        if self.q:
            queryset = queryset.filter(descripcion_campo_detallado_icontains=self.q)

        return queryset


##############################################################################
#########          Clase del autocomplete para Localidades          ##########
##############################################################################
class LocalidadesAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar listado del modelo Localidades.
    """
    def get_queryset(self):
        queryset = Localidad.objects.all()

        if self.q:
            queryset = queryset.filter(localidad_edit_icontains=self.q)

        return queryset


##############################################################################
#########       Clase del autocomplete para IEU Acreditadora        ##########
##############################################################################
class AcreditadoraAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para filtrar listado del modelo Acreditadora.
    """
    def get_queryset(self):
        queryset = Ieu.objects.all()

        if self.q:
            queryset = queryset.filter(ieu_acreditadora_edit_icontains=self.q)

        return queryset
