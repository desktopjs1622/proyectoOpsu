"""Vistas para el LOEU
"""
# Librerias Django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# Librerias de terceros
from dal import autocomplete

# Librerias desarrolladas por mi
from oeu.models import (
    AreaConocimiento, Carrera, Ieu, Localidad, SubAreaConocimiento,
    SubTipoInstitucion, TipoEspecificoInstitucion, TipoInstitucion)


# ########################################################################## #
class TipoIeuAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo TipoInstitucion
    """

    def get_queryset(self):
        queryset = TipoInstitucion.objects.filter(
            Q(cod_activacion='11000001') | Q(cod_activacion='10000001')
        )

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ########################################################################## #
class SubTipoIeuAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo TipoInstitucion
    """

    def get_queryset(self):

        tipo_ieu_edit = self.forwarded.get('tipo_ieu_edit', None)

        queryset = SubTipoInstitucion.objects.filter(
            Q(cod_activacion='11000011') | Q(cod_activacion='10000011')
        )

        if tipo_ieu_edit:
            queryset = queryset.filter(tipo_ieu=tipo_ieu_edit)

        if self.q:
            queryset = queryset.filter(nombre__icontains=self.q)

        return queryset


# ########################################################################## #
class TipoEspecificoIeuAutocomplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo SubTipoInstitucion
    """

    def get_queryset(self):

        sub_tipo_ieu_edit = self.forwarded.get('sub_tipo_ieu_edit', None)

        queryset = TipoEspecificoInstitucion.objects.filter(
            (Q(cod_activacion='11000111') | Q(cod_activacion='10000111'))
        )

        if sub_tipo_ieu_edit:
            queryset = queryset.filter(sub_tipo_ieu=sub_tipo_ieu_edit)

        if self.q:
            queryset = queryset.filter(
                nombre__icontains=self.q)

        return queryset


# ########################################################################## #
class IeuAutocomplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Institucion
    """

    def get_queryset(self):
        queryset = Ieu.objects.filter(
            (Q(cod_activacion='11001111') | Q(cod_activacion='10001111'))
        )

        if self.q:
            queryset = queryset.filter(
                institucion_ministerial__nombre__icontains=self.q)

        return queryset


# ########################################################################## #
class LocalidadIeuAutocomplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Localidad
    """

    def get_queryset(self):

        institucion_ministerial_edit = self.forwarded.get(
            'institucion_ministerial_edit', None)

        queryset = Localidad.objects.filter(
            (Q(cod_activacion='11011111') | Q(cod_activacion='10011111'))
        )

        if institucion_ministerial_edit:
            queryset = queryset.filter(ieu=institucion_ministerial_edit)

        if self.q:
            queryset = queryset.filter(
                nombre__icontains=self.q)

        return queryset


# ########################################################################## #
class AreaAutocomplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Area
    """

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return AreaConocimiento.objects.none()

        queryset = AreaConocimiento.objects.all()

        if self.q:
            queryset = queryset.filter(
                nombre_area_conocimiento__icontains=self.q)

        return queryset


# ########################################################################## #
class SubAreaAutocomplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo SubArea
    """

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return SubAreaConocimiento.objects.none()

        area = self.forwarded.get('id_area_conocimiento_edit', None)

        queryset = SubAreaConocimiento.objects.filter(
            id_area_conocimiento=area)

        if self.q:
            queryset = queryset.filter(
                nombre_subarea_conocimiento__icontains=self.q)

        return queryset


# ########################################################################## #
class CarreraAutocomplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Carrera
    """

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Carrera.objects.none()

        localidad = self.forwarded.get('localidad', None)

        queryset = Carrera.objects.filter(id_localidad_pub=localidad)

        if self.q:
            queryset = queryset.filter(nombre_carrera_pub__icontains=self.q)

        return queryset


# ########################################################################## #
#              Vistas para la gestión de los Modelos Complejos               #
# ########################################################################## #
class ListarModeloComplejo(ListView):
    """Con esta clase se puede listar los modelos que gestionan la estructura
    de datos de las institucuines de educación universitaría: TipoInstitucion,
    SubTipoInstitucion, TipoEspecificoInstitucion, Institucion, Localidad,
    Carrera.
    """

    filtro_por = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        filtro = self.request.GET.get("filtro")
        if filtro:
            filtro = {self.filtro_por: filtro}
            queryset = queryset.filter(**filtro)

        return queryset


# ########################################################################## #
class AgregarModeloComplejo(SuccessMessageMixin, CreateView):
    """Con esta clase se puede agregar los modelos que gestionan la estructura
    de datos de las institucuines de educación univeristaría: TipoInstitucion,
    SubTipoInstitucion, TipoEspecificoInstitucion, Institucion, Localidad,
    Carrera.
    """
    posicion = None
    revisor_edit = None
    SfcFormSet = None
    relacion_id = None

    def get_cod_activacion(self):
        """Prepara la brekera del código de activación de cada uno los modelos
        correspondientes para insertar o editar los registros en la base de
        datos
        """
        cod_activacion = list('00000000')
        for posicion in range(self.posicion, 8):
            cod_activacion[posicion] = '1'
        cod_activacion = ''.join(cod_activacion)

        return cod_activacion

    def get_context_data(self, **kwargs):
        contexto = super(AgregarModeloComplejo,
                         self).get_context_data(**kwargs)
        contexto['agregar'] = True

        contexto['sfc_form'] = self.SfcFormSet()

        return contexto

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.form_class)
        sfc_form = self.SfcFormSet(self.request.POST)
        if (form.is_valid() and sfc_form.is_valid()):
            return self.form_valid(form, sfc_form)
        else:
            return self.form_invalid(form, sfc_form)

    def form_valid(self, form, sfc_form):
        self.object = form.save(commit=False)
        self.object.cod_activacion = self.get_cod_activacion()
        self.object.publicar = False
        with transaction.atomic():
            self.object.save()

            sfc_form.instance = self.object
            sfc_form.save()

            # Ahora guardo el regisro en la tabla de revisores edit.
            filtro = {
                self.relacion_id: self.object,
                'persona': self.request.user
                }
            rev = self.revisor_edit(**filtro)
            rev.save()
            # cursor = connection.cursor()
            # tabla = self.revisor_edit._meta.db_table.replace('"', '')
            # insert = "INSERT INTO " + tabla
            # values = " VALUES (DEFAULT, %s, %s)"
            # query = insert + values % (self.object.id, self.request.user.pk)
            # cursor.execute(query)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, sfc_form):
        return self.render_to_response(self.get_context_data(
            form=form, sfc_form=sfc_form))


# ########################################################################## #
class EditarModeloComplejo(SuccessMessageMixin, UpdateView):
    """Con esta clase se puede editar los modelos que gestionan la estructura
    de datos de las institucuines de educación univeristaría: TipoInstitucion,
    SubTipoInstitucion, TipoEspecificoInstitucion, Institucion, Localidad,
    Carrera.
    """
    posicion = None
    revisor_edit = None
    SfcFormSet = None
    relacion_id = None

    def __init__(self, *args, **kwargs):
        super(EditarModeloComplejo, self).__init__(*args, **kwargs)
        # Para almacenar el código activo e inactivo
        self.cod_acti = None
        self.cod_inac = None
        self.object = None

    def get_cod_activacion(self):
        """Prepara la brekera del código de activación de cada uno los modelos
        correspondientes para insertar o editar los registros en la base de
        datos
        """
        self.object = self.get_object()
        if self.object.cod_activacion[self.posicion] == '1':
            self.cod_acti = self.object.cod_activacion
            lista = list(self.cod_acti)
            lista[self.posicion] = '0'
            self.cod_inac = ''.join(lista)
            activo = True
        else:
            self.cod_inac = self.object.cod_activacion
            lista = list(self.cod_inac)
            lista[self.posicion] = '1'
            self.cod_acti = ''.join(lista)
            activo = False

        return activo

    def get_revisado(self, cod_activacion):
        """Prepara la brekera del código de activación de cada uno los modelos
        correspondientes para insertar o editar los registros en la base de
        datos
        """
        cod_activacion = list(cod_activacion)
        cod_activacion[1] = '0'
        cod_activacion = ''.join(cod_activacion)

        return cod_activacion

    def mensaje_inactivacion(self):
        """Prepara la brekera del código de activación de cada uno los modelos
        correspondientes para insertar o editar los registros en la base de
        datos
        """
        self.object = self.get_object()

        mensaje = 'Este registro se encuentra inactivo:'

        if self.posicion <= 7 and self.object.cod_activacion[7] == '0':
            mensaje += '<br><b>Tipo IEU</b>: Inactivo'
        if self.posicion <= 6 and self.object.cod_activacion[6] == '0':
            mensaje += '<br><b>Sub Tipo Institucion</b>: Inactivo'
        if self.posicion <= 5 and self.object.cod_activacion[5] == '0':
            mensaje += '<br><b>Tipo Específico IEU</b>: Inactivo'
        if self.posicion <= 4 and self.object.cod_activacion[4] == '0':
            mensaje += '<br><b>IEU</b>: Inactivo'
        if self.posicion <= 3 and self.object.cod_activacion[3] == '0':
            mensaje += '<br><b>Localidad</b>: Inactivo'
        if self.posicion <= 2 and self.object.cod_activacion[2] == '0':
            mensaje += '<br><b>Programa Académico</b>: Inactivo'

        return mark_safe(mensaje)

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        contexto = super(EditarModeloComplejo, self).get_context_data(**kwargs)
        contexto['agregar'] = False
        contexto['activo'] = self.get_cod_activacion()
        if not contexto['activo']:
            messages.error(self.request, self.mensaje_inactivacion())

        if self.object.cod_activacion[0] == '0' and self.object.cod_activacion[1] == '0':
            messages.warning(self.request, 'Estás editando un nuevo registro\
            que aún no ha sido publicado')

        if self.request.POST:
            contexto['sfc_form'] = self.SfcFormSet(
                self.request.POST, instance=self.object)
        else:
            contexto['sfc_form'] = self.SfcFormSet(instance=self.object)
        return contexto

    def post(self, request, *args, **kwargs):
        contexto = self.get_context_data(**kwargs)
        form = self.get_form(self.form_class)
        sfc_form = contexto['sfc_form']

        if form.is_valid() and sfc_form.is_valid():
            return self.form_valid(form, sfc_form)

        return self.form_invalid(form, sfc_form)

    def form_valid(self, form, sfc_form):
        self.object = self.get_object()
        editor = self.object.editor
        cod_activacion = self.object.cod_activacion
        formulario = form.save(commit=False)

        if formulario.publicar and self.request.user.has_perm('oeu.post_oeu'):
            formulario.editor = self.request.user
            if formulario.cod_activacion == 'True':
                formulario.cod_activacion = self.get_revisado(self.cod_acti)
            elif formulario.cod_activacion == 'False':
                formulario.cod_activacion = self.get_revisado(self.cod_inac)
        else:
            formulario.cod_activacion = self.get_revisado(cod_activacion)
            formulario.editor = editor

        with transaction.atomic():
            formulario.save()
            sfc_form.instance = formulario
            sfc_form.save()

            """ Ahora guardo el regisro en la tabla de revisores en caso de que
            el revisor ya no esté asociado. """

            if not formulario.publicar:
                filtro = {
                    self.relacion_id: self.object,
                    'persona': self.request.user.pk
                }
                revisor = self.revisor_edit.objects.filter(**filtro).exists()

                if not revisor:
                    filtro = {
                        self.relacion_id: self.object,
                        'persona': self.request.user
                        }
                    rev = self.revisor_edit(**filtro)
                    rev.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, sfc_form):
        return self.render_to_response(self.get_context_data(
            form=form,
            sfc_form=sfc_form))


# ########################################################################## #
class EliminarModeloComplejo(SuccessMessageMixin, DeleteView):
    """Con esta clase se puede eliminar los modelos que gestionan la estructura
    de datos de las institucuines de educación univeristaría: TipoInstitucion,
    SubTipoInstitucion, TipoEspecificoInstitucion, Institucion, Localidad,
    Carrera.
    """
    relacion = None
    rel_sfc = None
    relacion_id = None

    def __init__(self, *args, **kwargs):
        super(EliminarModeloComplejo, self).__init__(*args, **kwargs)
        # Para almacenar el código activo e inactivo
        self.relacionado = None
        self.object = None

    def get_context_data(self, **kwargs):
        contexto = super(EliminarModeloComplejo,
                         self).get_context_data(**kwargs)

        filtro = {self.relacion_id: self.kwargs['pk']}
        self.relacionado = self.relacion.objects.filter(**filtro).exists()

        if not self.relacionado:
            self.relacionado = self.rel_sfc.objects.filter(**filtro).exists()

        contexto['relacionado'] = self.relacionado

        return contexto

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data(**kwargs)

        if not self.relacionado:
            self.object.delete()
            messages.success(self.request, self.success_message)

        return HttpResponseRedirect(self.get_success_url())
