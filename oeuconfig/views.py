"""Vistas para el LOEU
"""
# Librerias Django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

# Librerias de terceros
from oeuconfig.forms import SfcForm
from oeuconfig.models import SoporteFormalCambio

# Librerias desarrolladas por mi
from oeu.models import (
    ActividadCulturalLocalidad, AgrupacionCivicaLocalidad,
    AyudaEconomicaLocalidad, CorreoLocalidad, DisciplinaDeportivaLocalidad,
    OrganizacionEstudiantilLocalidad, RedSocialLocalidad, TelefonoLocalidad)

##############################################################################
#          Vistas para la gestión de los modelos simples, ejemplos:          #
#        TipoAyudaEconomica, TipoActividadCUltural, TipoCarrera, etc.        #
##############################################################################


##############################################################################
class AgregarModeloSimple(SuccessMessageMixin, CreateView):
    """Esta clase sirve para agregar todos los modelos que son auxiliares a
    otros modelos, por ejemplo: TipoAyudaEconomica, TipoActividadCUltural,
    TipoCarrera, etc. Para ver su funcionamiento dirijase a las URL's
    """
    pass


##############################################################################
class EditarModeloSimple(SuccessMessageMixin, UpdateView):
    """Esta clase sirve para editar todos los modelos que son auxiliares a
    otros modelos, por ejemplo: TipoAyudaEconomica, TipoActividadCUltural,
    TipoCarrera, etc. Para ver su funcionamiento dirijase a las URL's
    """
    pass


##############################################################################
class EliminarModeloSimple(SuccessMessageMixin, DeleteView):
    """Esta clase sirve para eliminar todos los modelos que son auxiliares a
    otros modelos, por ejemplo: TipoAyudaEconomica, TipoActividadCUltural,
    TipoCarrera, etc. Para ver su funcionamiento dirijase a las URL's.
    Siempre y cuando no tengo objetos dependientes.
    """

    relacion = None
    relacion_id = None

    def __init__(self, *args, **kwargs):
        super(EliminarModeloSimple, self).__init__(*args, **kwargs)
        # Para almacenar el código activo e inactivo
        self.relacionado = None
        self.object = None

    def get_context_data(self, **kwargs):
        contexto = super(EliminarModeloSimple, self).get_context_data(**kwargs)
        if self.relacion and self.relacion_id:

            filtro = {self.relacion_id: self.kwargs['pk']}
            self.relacionado = self.relacion.objects.filter(**filtro).exists()

        contexto['relacionado'] = self.relacionado

        return contexto

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data(**kwargs)

        if not self.relacionado:
            messages.success(self.request, self.success_message)

            return self.delete(request, *args, **kwargs)

        return HttpResponseRedirect(self.get_success_url())


##############################################################################
#          Modulo tipo instancia administrativa clase para eliminar          #
#        dependencias directas con el modelo instancia administrativa        #
##############################################################################

##############################################################################
class EliminarInstanciaAdministrativa(SuccessMessageMixin, DeleteView):
    """Esta clase sirve para eliminar todos los modelos que tienen una relación
    con la Instancia Administrativa
    """

    def __init__(self, *args, **kwargs):
        super(EliminarInstanciaAdministrativa, self).__init__(*args, **kwargs)
        # Para almacenar el código activo e inactivo
        self.relacionado = None
        self.object = None

    def get_context_data(self, **kwargs):
        contexto = super(EliminarInstanciaAdministrativa,
                         self).get_context_data(**kwargs)

        pki = self.kwargs['pk']
        cli = CorreoLocalidad
        tli = TelefonoLocalidad
        aei = AyudaEconomicaLocalidad
        acli = ActividadCulturalLocalidad
        ddli = DisciplinaDeportivaLocalidad
        oeli = OrganizacionEstudiantilLocalidad
        acli = AgrupacionCivicaLocalidad
        rsli = RedSocialLocalidad

        if cli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif tli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif aei.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif acli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif ddli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif oeli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif acli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        elif rsli.objects.filter(instancia_administrativa=pki).exists():
            contexto['relacionado'] = True
        else:
            contexto['relacionado'] = False

        return contexto

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data(**kwargs)

        if not self.relacionado:
            messages.success(self.request, self.success_message)

            return self.delete(request, *args, **kwargs)

        return HttpResponseRedirect(self.get_success_url())

##############################################################################
#          Modulo tipo instancia administrativa clase para registrar         #
#                   el modelo soporte formal de cambio                       #
##############################################################################


class AgregarSfc(SuccessMessageMixin, CreateView):
    """Con esta clase se puede agregar los Soportes Formales de Cambio.
    """
    model = SoporteFormalCambio
    form_class = SfcForm
    template_name = 'soporte_formal_cambio_formulario.html'
    success_url = reverse_lazy('oeuconfig:listar-soporte-formal-cambio')


class EditarSfc(SuccessMessageMixin, UpdateView):
    """Con esta clase se puede editar los Soportes Formales de Cambio.
    """
    model = SoporteFormalCambio
    form_class = SfcForm
    template_name = 'soporte_formal_cambio_formulario.html'
    success_url = reverse_lazy('oeuconfig:listar-soporte-formal-cambio')
