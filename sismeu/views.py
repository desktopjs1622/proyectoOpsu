# Librerias Standard
import datetime

# Librerias Django
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, UpdateView
from django.utils.safestring import mark_safe


# Librerias de terceros
from dal import autocomplete

from sismeu.forms import (ClinicaForm,
                          HistoriaForm, MotivoInactivacionForm, RegionEstadoForm,
                          REGIONESTADOFORMSET, RegionForm, inlineformset_factory, CONVENIO_CLINICA_FORMSET,
                          ContactoClinicaForm, RESPONSABLEREGIONALFORMSET)

# Librerias desarrolladas por mi
from globales.models import Estado, Municipio, Parroquia

# Librerias en carpetas locales
from sismeu.models import (
    Clinica, HistoricoClinica, MotivoInactivacion, Region,
    Departamento, TelefonoClinica, RegionEstado, ResponsableRegional, AuditoriaClinica)

# Create your views here.
##############################################################################
#########                            Index de Sismeu                ##########
##############################################################################


def index(request):
    """ Pagina inicial
    """
    contexto = {}
    # Conteo de las clinicas en general
    contexto['clinica'] = Clinica.objects.all().count()
    # Busco los estados que pertenecen a la región del usuario registrado
    r_e = ResponsableRegional.objects.get(responsable=request.user).region.estado.all()
    contexto['clinica_region'] = Clinica.objects\
        .filter(parroquia__idmunicipioglobal__idestadoglobal__in=r_e).count()  # Conteo de las clinicas ubicadas en la región
    contexto['activa'] = HistoricoClinica.objects.filter(
        fecha_inactivacion=None).count()  # Conteo de las clinicas activas
    return render(request, 'index_sismeu.html', contexto)

##############################################################################
#########                          Listado de clinica               ##########
##############################################################################


def lista_clinica(request):
    """ Busco solo las clinicas ubicadas en la región donde la persona registrada es responsable 
    """

    contexto = {}
    # Verifico que el usuario registrado se administrador
    if request.user.groups.filter(name='AdminSismeu').exists():
        # Listo las clinicas Completa si el usuario es administrador
        contexto['clinicas'] = Clinica.objects.all()
    else:  # si el usuario no es administrador
        # Busco los estados pertenecientes a la region del usuario
        r_e = Region.objects.get(responsable=request.user).estado.all()
        contexto['clinicas'] = Clinica.objects\
            .filter(parroquia__idmunicipioglobal__idestadoglobal__in=r_e)  # listo las clinicas ubicadas en la region del contacto
    return render(request, 'vista_general.html', contexto)

##############################################################################
#########              registro y edito las clinicas                ##########
##############################################################################


def formulario_clinica(request, id_clinica=None):
    """ Función para crear una clínica y editar si ya esta creada """

    contexto = {}
    if id_clinica is None:
        contexto['form'] = ClinicaForm()
        contexto['formset'] = CONVENIO_CLINICA_FORMSET()
    else:
        contexto['id_clinica'] = Clinica.objects.get(pk=id_clinica)
        contexto['form'] = ClinicaForm(instance=contexto['id_clinica'])
        contexto['formset'] = CONVENIO_CLINICA_FORMSET(
            instance=contexto['id_clinica'])
    if request.method == 'POST':
        if id_clinica is None:
            contexto['form'] = ClinicaForm(request.POST)
            contexto['formset'] = CONVENIO_CLINICA_FORMSET(request.POST)
            mensaje = '¡Se agrego la clinica exitosamente!'
            direccion = reverse('sismeu:vista_general')
        else:
            contexto['form'] = ClinicaForm(
                request.POST, instance=contexto['id_clinica'])
            contexto['formset'] = CONVENIO_CLINICA_FORMSET(
                request.POST, instance=contexto['id_clinica'])
            mensaje = '¡Se actualizo la clinica exitosamente!'
            direccion = reverse('sismeu:editar_clinica', args=[id_clinica])
        if contexto['form'].is_valid() and contexto['formset'].is_valid():
            with transaction.atomic():
                b = contexto['form'].save(commit=False)
                b.editor = request.user
                b.save()
                contexto['formset'].instance = b
                contexto['formset'].save()
                messages.success(request, mensaje)
        return HttpResponseRedirect(direccion)
    return render(request, "clinica_formulario.html", contexto)

##############################################################################
#########               Detallo la clinica y su estatus             ##########
##############################################################################


def detalles_clinica(request, id_clinica):
    """ Detallo las clinicas y reviso su historico para saber su estatus 
    """

    contexto = {}
    contexto['clinica'] = Clinica.objects.get(pk=id_clinica)
    if contexto['clinica'].historicoclinica_set.all().exists() == True:
        contexto['historia'] = contexto['clinica'].historicoclinica_set.all()
    else:
        contexto['historia'] = False
    return render(request, 'detalles_clinica.html', contexto)

##############################################################################
#########              Elimino la clinica                           ##########
##############################################################################


def eliminar_clinica(request, id_clinica):
    """ Elimino la clinica sino tiene un historico creado
    """

    contexto = {}
    contexto['clinica'] = Clinica.objects.get(pk=id_clinica)
    contexto['historia_clinica'] = HistoricoClinica.objects.filter(clinica_id=contexto['clinica'])\
        .count()
    if request.method == 'POST':
        if contexto['historia_clinica'] == 0:
            contexto['clinica'].delete()
            messages.success(request, 'Se elimino correctamente la clinica')
        else:
            messages.error(request, 'La clinica tiene registros existentes\
            , verifique e intente de nuevo')
        return HttpResponseRedirect(reverse('sismeu:vista_general'))
    return render(request, 'eliminar_clinica.html', contexto)

##############################################################################
#########               historico de la Clinica                     ##########
##############################################################################


def activar_clinica(request, id_clinica):
    """ Activo la clinica y le creo un historio asignando el responsable automaticamente
    """
    contexto = {}
    contexto['clinica'] = Clinica.objects.get(pk=id_clinica)
    contexto['responsable'] = request.user
    print(contexto['responsable'])
    if contexto['clinica'].historicoclinica_set.all().exists() == False:
        HistoricoClinica.objects.create(
            clinica=contexto['clinica'],
            responsable_activacion=contexto['responsable'],
        )
        messages.success(request, '¡Activacion exitosa!')
    elif contexto['clinica'].historicoclinica_set.all().exists() == True:
        if contexto['clinica'].historicoclinica_set.all().latest('pk').fecha_inactivacion != None:

            HistoricoClinica.objects.create(
                clinica=contexto['clinica'],
                responsable_activacion=contexto['responsable'],
            )
            messages.success(request, '¡Activación Exitosa!')
        else:
            messages.error(request, '¡La clinica aun se encuentra activa!')
    return HttpResponseRedirect(reverse('sismeu:vista_general'))

##############################################################################
#########                  Desactivar Clinica                       ##########
##############################################################################


def desactivar_clinica(request, id_clinica=None):
    """ Asigno fecha de inactivación y responsable al historico para desactivar la clinica
    """
    contexto = {}
    contexto['clinica'] = Clinica.objects.get(pk=id_clinica)
    contexto['responsable'] = request.user
    contexto['historia'] = contexto['clinica'].historicoclinica_set.all().latest('pk')
    historia_id = contexto['clinica'].historicoclinica_set.get(
        pk=contexto['historia'].pk)
    if request.method == 'GET':
        contexto['form'] = HistoriaForm(instance=historia_id)
    else:
        contexto['form'] = HistoriaForm(request.POST, instance=historia_id)
        if contexto['form'].is_valid():
            form = contexto['form'].save(commit=False)
            form.fecha_inactivacion = timezone.now()
            form.responsable_inactivacion = contexto['responsable']
            form.save()
            messages.success(request, '¡Clinica desactivada exitosamente!')
        return HttpResponseRedirect(reverse('sismeu:vista_general'))
    return render(request, 'desactivar_clinica.html', contexto)

##############################################################################
#########               Detalles de la historia                     ##########
##############################################################################


def detalle_historia(request, historico_id):
    """ Reviso las historias para ver los motivos de inactivación
    """
    contexto = {}
    contexto['historico_id'] = historico_id
    contexto['historia'] = HistoricoClinica.objects.get(pk=historico_id)
    return render(request, 'detalle_historia.html', contexto)

##############################################################################
#########                 Registro de Regiones                      ##########
##############################################################################

def lista_region(request):
    """  Listado de regiones, solo para administradores
    """

    contexto = {}
    contexto['region'] = Region.objects.all()
    return render(request, 'region_lista.html', contexto)

##############################################################################

def registro_region(request, region_id=None):

    """ Función para crear y editar region y sus estados
    """
    contexto = {}
    if region_id is None:
        contexto['form'] = RegionForm()
        contexto['formset'] = REGIONESTADOFORMSET()
        contexto['formset2'] = RESPONSABLEREGIONALFORMSET()
    else:
        contexto['region'] = Region.objects.get(pk=region_id)
        contexto['form'] = RegionForm(instance=contexto['region'])
        contexto['formset'] = REGIONESTADOFORMSET(instance=contexto['region'])
        contexto['formset2'] = RESPONSABLEREGIONALFORMSET(instance=contexto['region'])
    if request.method == 'POST':
        if region_id is None:
            contexto['form'] = RegionForm(request.POST)
            contexto['formset'] = REGIONESTADOFORMSET(request.POST)
            contexto['formset2'] = RESPONSABLEREGIONALFORMSET(request.POST)
            mensaje = '¡Se agrego de manera exitosa la región!'
        else:
            contexto['form'] = RegionForm(
                request.POST, instance=contexto['region'])
            contexto['formset'] = REGIONESTADOFORMSET(
                request.POST, instance=contexto['region'])
            contexto['formset2'] = RESPONSABLEREGIONALFORMSET(
                request.POST, instance=contexto['region'])

            mensaje = '¡Se actualizo la región exitosamente!'
        if contexto['form'].is_valid() and contexto['formset'].is_valid() and contexto['formset2'].is_valid():
            with transaction.atomic():
                a = contexto['form'].save()
                contexto['formset'].instance = a
                contexto['formset'].save()
                contexto['formset2'].instance = a
                contexto['formset2'].save()
                messages.success(request, mensaje)
        return HttpResponseRedirect(reverse('sismeu:lista_region'))
    return render(request, 'registro_region.html', contexto)

##############################################################################

def eliminar_region(request, region_id):
    """ Elimino la clínica sino tiene un historico creado
    """

    contexto = {}
    contexto['region'] = Region.objects.get(pk=region_id)
    contexto['estado'] = contexto['region'].estado.count()
    if request.method == 'POST':
        if contexto['estado'] == 0:
            contexto['region'].delete()
            messages.success(request, 'Se elimino correctamente la región')
        else:
            messages.error(request, 'La region tiene Estados existentes\
            , verifique e intente de nuevo')
        return HttpResponseRedirect(reverse('sismeu:lista_region'))
    return render(request, 'eliminar_region.html', contexto)

##############################################################################
#########                Contacto de la clínica                     ##########
##############################################################################

def contacto_clinica(request, id_clinica, telefono_id=None):

    contexto = {}
    contexto['clinica'] = Clinica.objects.get(pk=id_clinica)
    if telefono_id is None:
        contexto['form'] = ContactoClinicaForm()
    else:
        contexto['telefono'] = TelefonoClinica.objects.get(pk=telefono_id)
        contexto['form'] = ContactoClinicaForm(instance=contexto['telefono'])
    if request.method == 'POST':
        if telefono_id is None:
            contexto['form'] = ContactoClinicaForm(request.POST)
            mensaje = '¡Se agrego de manera exitosa el Telefono y contacto!'
        else:
            contexto['form'] = ContactoClinicaForm(request.POST, instance=contexto['telefono'])
            mensaje = '¡Se actualizo el telefono exitosamente!'
        if contexto['form'].is_valid():
            with transaction.atomic():
                form = contexto['form'].save(commit=False)
                form.clinica = contexto['clinica']
                form.save()
                messages.success(request, mensaje)
        return HttpResponseRedirect(reverse('sismeu:editar_clinica', args=[id_clinica]))
    return render(request, 'telefono_clinica.html', contexto)

#############################################################################

def eliminar_telefono(request, telefono_id, id_clinica):
    """ Elimino el número telefonico
    """
    contexto = {}
    contexto['clinica'] = Clinica.objects.get(pk=id_clinica)
    contexto['telefono'] = TelefonoClinica.objects.get(pk=telefono_id)
    if request.method == 'POST':
        contexto['telefono'].delete()
        messages.success(request, 'Se elimino correctamente el telefono')
        return HttpResponseRedirect(reverse('sismeu:editar_clinica', args=[id_clinica]))
    return render(request, 'eliminar_telefono.html', contexto)

#############################################################################

def auditoria_clinica(request):

    contexto = {}
    contexto['auditoria'] = AuditoriaClinica.objects.all().order_by('-id')
    return render(request, 'auditoria_lista.html', contexto)


def detalle_auditoria(request, auditoria_id):
    """ Reviso las historias para ver los motivos de inactivación
    """
    contexto = {}
    contexto['auditoria_id'] = auditoria_id
    contexto['auditoria'] = AuditoriaClinica.objects.get(pk=auditoria_id)
    contexto['clinica'] = Clinica.objects.get(rif=contexto['auditoria'].rif)
    return render(request, 'auditoria_clinica.html', contexto)
    
##############################################################################
#########          Clase del autocomplete de parroquias             ##########
##############################################################################
class EstadoRegionAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        e = RegionEstado.objects.all().values('estado')
        if e:
            qs = Estado.objects.exclude(idestadoglobal__in=e)
        else:
            qs = Estado.objects.all()

        return qs

class EstadoAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        r_e = Region.objects.get(responsable=self.request.user).estado.all()
        if r_e:
            qs = Estado.objects.filter(idestadoglobal__in=r_e)
        else:
            qs = None

        return qs


class MunicipioAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        estado = self.forwarded.get('estado', None)
        if estado:
            qs = Municipio.objects.filter(idestadoglobal=estado)
        else:
            qs = None

        return qs



""" Filtro de parroquias pertenecientes a los estados de la region de la persona resposable
"""


class ParroquiaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        municipio = self.forwarded.get('municipio', None)
        if municipio:
            qs = Parroquia.objects.filter(idmunicipioglobal=municipio)
        else:
            qs = None

        return qs



##############################################################################
class EditarModelo(SuccessMessageMixin, UpdateView):
    """Con esta clase se puede editar el modelo de clínica
    """
    FormSet = None

    def __init__(self, *args, **kwargs):
        super(EditarModelo, self).__init__(*args, **kwargs)

        self.object = None

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        contexto = super(EditarModelo, self).get_context_data(**kwargs)
        contexto['agregar'] = False
        if self.request.POST:
            contexto['formset'] = self.FormSet(
                self.request.POST, instance=self.object)
        else:
            contexto['formset'] = self.FormSet(instance=self.object)
        return contexto

    def post(self, request, *args, **kwargs):
        contexto = self.get_context_data(**kwargs)
        form = self.get_form(self.form_class)
        formset = contexto['formset']

        if contexto['form'].is_valid() and contexto['formset'].is_valid():
            with transaction.atomic():
                b = contexto['form'].save()
                contexto['formset'].instance=b
                contexto['formset'].save()

        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form, formset):
        # self.object = self.get_object()
        # formulario = form.save(commit=False)

        # with transaction.atomic():
        #     formulario.save()
        #     formset.instance = formulario
        #     formset.save()


        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(
            form=form,
            formset=formset))
