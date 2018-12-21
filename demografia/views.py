# -*- coding: utf-8 -*-
# Librerias Standard

import datetime
import urllib
from io import BytesIO

# Librerias Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Value
from django.db.models.functions import Concat
from django.forms import formset_factory, modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

# Librerias de terceros
from cuenta.forms import PersonaForm
from cuenta.models import Persona
from dal import autocomplete

# Librerias desarrolladas por mi
from demografia.forms import (
    HogarForm, MiembrohogarForm, SaludPersonaForm, ViviendaForm)
from demografia.models import (
    Condicionfisicavivienda, Hogar, Miembrohogar, Salud, Tipodiscapacidad,
    Vivienda, Vocero, Zona)
from demografia.reportes import misReportes


###################################################################################################
# @login_required
def index(request):
    return render(request, 'index.html')


###################################################################################################
class PersonaList(FormMixin, ListView):
    """
    Clases para el modelo persona: lista personas, edita personas y agrega personas (misma clase) y
    elimina personas
    """
    model = Miembrohogar
    form_class = MiembrohogarForm
    context_object_name = 'listaPersona'
    template_name = 'demografia/listaPersona.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()

        context = self.get_context_data(
            object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        if self.form.is_valid():
            self.form.save()
            return HttpResponseRedirect('')
        else:
            return self.get(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonaList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        # Determino la comunidad a la que pertenece el vocero que
        # acaba de logearse.
        vocero = Vocero.objects.get(persona=self.request.user)

        # Cargo todos los miembros que pertencen a la familia que estoy pasando como parametro garantizando que sea un hogar/familia
        # que el usuario auntenticado pueda modificar. Asi evito que algun vivo
        # modifque el url para modificar otro hogar/familia.

        return Miembrohogar.objects.filter(hogar=vocero.zona.vivienda_set.get(idvivienda=self.kwargs['idVivienda']).hogar_set.get(idhogar=self.kwargs['idHogar']))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(PersonaList, self).get_context_data(**kwargs)

        # Ahora cargo todos los hogares o familias que habitan en la vivienda
        contexto['hogar'] = Hogar.objects.get(pk=self.kwargs['idHogar'])

        contexto['form'] = self.get_form()

        return contexto


###################################################################################################
@login_required
def persona(request, idPersona=None, idHogar=None, idVivienda=None, accion=None):
    contexto = {} # Diccionario de contexto para la plantilla
    contexto['vivienda'] = idVivienda
    contexto['hogar'] = idHogar
    fecha_actual = datetime.date.today()
    contexto['hoy'] = str(int(fecha_actual.day) - 1) + "/" + \
        str(fecha_actual.month) + "/" + str(fecha_actual.year)
    if accion == 0:
        contexto['active'] = 'Añadir persona'
        contexto['form'] = PersonaForm()
        contexto['persona'] = ''
        contexto['cne'] = ''
    elif accion == 1:
        contexto['active'] = 'Mostrar persona'
        contexto['persona'] = Persona.objects.get(pk=idPersona)
        contexto['form'] = PersonaForm(instance=contexto['persona'])
        contexto['cne'] = ''
    elif accion == 2:
        contexto['active'] = 'Editar persona'
        contexto['persona'] = Persona.objects.get(pk=idPersona)
        try:
            #url = urllib.urlopen("http://www.cne.gov.ve/web/registro_electoral/ceRE.php?nacionalidad=" + persona.letracedulaidentidad + "&cedula=" + str(persona.cedulaidentidad))
            #cne = strip_tags(url.read().decode('utf-8')).replace("\t", "").replace("\n", "").replace("\r", "")
            contexto['cne'] = None
        except ValueError:
            contexto['cne'] = None
        if contexto['cne']:
            pos_parroquia = contexto['cne'].find(u'Parroquia') + 10
            pos_centro = contexto['cne'].find(u'Centro')
            contexto['cne'] = contexto['cne'][pos_parroquia:pos_centro]
        else:
            contexto['cne'] = None
        contexto['form'] = PersonaForm(instance=contexto['persona'], initial={'cne': contexto['cne']})
    elif accion == 3:
        contexto['active'] = 'Eliminar persona'
        contexto['persona'] = Miembrohogar.objects.get(persona=idPersona)

    if request.method == 'POST':
        ##########                       Estoy guardando los datos                       ##########
        if accion == 0:
            contexto['form'] = PersonaForm(request.POST, request.FILES)
        elif accion == 2:
            contexto['form'] = PersonaForm(request.POST, request.FILES, instance=contexto['persona'])
        elif accion == 3:
            contexto['persona'].delete()
            return HttpResponseRedirect(reverse('demografia:hogar', args=(idVivienda, idHogar)))

        if contexto['form'].is_valid():
            if accion == 0 or accion == 2:
                contexto['form'].save()
                return HttpResponseRedirect(reverse('demografia:hogar', args=(idVivienda, idHogar)))
        else:
            return render(request, 'demografia/persona.html', contexto)
    elif accion == 3:
        ##########                       Estoy eliminando los datos                      ##########
        return render(request, 'demografia/eliminarPersona.html', contexto)
    else:
        ##########                        Estoy editando los datos                       ##########
        return render(request, 'demografia/persona.html', contexto)


###################################################################################################
@login_required
def saludPersona(request, idPersona=None, idHogar=None, idVivienda=None, accione=None):
    contexto = {} # Diccionario de contexto para la plantilla
    contexto['vivienda'] = idVivienda
    contexto['hogar'] = idHogar
    contexto['persona'] = Persona.objects.get(pk=idPersona)
    contexto['tipoDiscapacidad'] = Tipodiscapacidad.objects.filter()
    if accione == 4:
        contexto['active'] = 'Mostrar persona'
    elif accione == 5:
        contexto['active'] = 'Editar persona'

    try:
        contexto['salud_persona'] = Salud.objects.get(pk=idPersona)
    except:
        contexto['salud_persona'] = None

    if contexto['salud_persona']:
        contexto['form'] = SaludPersonaForm(instance=contexto['salud_persona'])
        contexto['lista_patologia'] = contexto['salud_persona'].patologia.all()
        contexto['lista_discapacidad'] = contexto['salud_persona'].discapacidad.all()
        contexto['lista_tipo_poyo'] = contexto['salud_persona'].tipoapoyo.all()
    else:
        contexto['form'] = SaludPersonaForm(initial={'persona': idPersona})
        contexto['lista_patologia'] = None
        contexto['lista_discapacidad'] = None
        contexto['lista_tipo_poyo'] = None

    if request.method == 'POST':
        if contexto['salud_persona']:
            contexto['form'] = SaludPersonaForm(
                request.POST, request.FILES, instance=contexto['salud_persona'])
        else:
            contexto['form'] = SaludPersonaForm(request.POST, request.FILES, initial={'persona': idPersona})

        if contexto['form'].is_valid():
            contexto['form'].save()
            return HttpResponseRedirect(reverse('demografia:hogar', args=(idVivienda, idHogar)))
    return render(request, 'demografia/saludPersona.html', contexto)


###################################################################################################
@login_required
def eliminarPersona(request, idPersona=None, idHogar=None, idVivienda=None):
    contexto = {}  # Diccionario de contexto para la plantilla
    contexto['vivienda'] = idVivienda
    contexto['hogar'] = idHogar
    contexto['persona'] = Miembrohogar.objects.get(persona=idPersona)
    if request.method == 'POST':
        contexto['persona'].delete()
        return HttpResponseRedirect(reverse('hogar', args=(idVivienda, idHogar)))
    return render(request, 'demografia/eliminarPersona.html', contexto)


###################################################################################################
class HogarList(FormMixin, ListView):
    """
    Clases para el modelo hogar: lista y agrega, edita, elimina hogares y agrega miembros a los
    hogares
    """
    model = Hogar
    form_class = HogarForm
    context_object_name = 'listaHogar'
    template_name = 'demografia/listaHogar.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()

        context = self.get_context_data(
            object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        if self.form.is_valid():
            self.form.save()
            return HttpResponseRedirect('')
        else:
            return self.get(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HogarList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        # Determino la comunidad a la que pertenece el vocero que
        # acaba de logearse.
        vocero = Vocero.objects.get(persona=self.request.user)

        return Hogar.objects.filter(vivienda=vocero.zona.vivienda_set.get(idvivienda=self.kwargs['idVivienda']))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(HogarList, self).get_context_data(**kwargs)

        # Busco la vivienda que paso en el parametro
        contexto['vivienda'] = Vivienda.objects.get(pk=self.kwargs['idVivienda'])

        # Cargar la zona de la vivienda
        contexto['cantidadMiembroHogar'] = Miembrohogar.objects.filter(
            hogar__in=contexto['vivienda'].hogar_set.all()).count()

        return contexto


###################################################################################################
@login_required
def editarHogar(request, idHogar=None, idVivienda=None):
    contexto = {}  # Diccionario de contexto para la plantilla
    contexto['vivienda'] = idVivienda
    contexto['hogar'] = Hogar.objects.get(pk=idHogar)
    contexto['form'] = HogarForm(instance=contexto['hogar'])

    if request.method == 'POST':
        contexto['form'] = HogarForm(request.POST, instance=contexto['hogar'])
        if contexto['form'].is_valid():
            contexto['form'].save()
            return HttpResponseRedirect(reverse('vivienda', args=(idVivienda,)))
    return render(request, 'demografia/editarHogar.html', contexto)


###################################################################################################
@login_required
def eliminarHogar(request, idHogar=None, idVivienda=None):
    contexto = {}  # Diccionario de contexto para la plantilla
    contexto['vivienda'] = idVivienda
    contexto['hogar'] = Hogar.objects.get(pk=idHogar)
    if request.method == 'POST':
        contexto['hogar'].delete()
        return HttpResponseRedirect(reverse('vivienda', args=(idVivienda,)))
    return render(request, 'demografia/eliminarHogar.html', contexto)


# @login_required
# def agregarMiembroHogar(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         formset = PersonaFormSet(request.POST, request.FILES)
#         # check whether it's valid:
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect('')
#     else:
#         return render(request, 'demografia/persona.html', {'formset': formset, 'persona': persona})


###################################################################################################
class ViviendaList(ListView):
    """
    Clases para el modelo vivienda: lista, grega, edita y elimina viviendas
    """
    context_object_name = 'listaVivienda'
    template_name = 'demografia/zona.html'
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ViviendaList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Ahora cargo todas las viviendas de todas las zonas del consejo
        # comunal

        # Determino la comunidad a la que pertenece el vocero que
        # acaba de logearse.
        vocero = Vocero.objects.get(persona=self.request.user)

        # return Vivienda.objects.filter(zona=Zona.objects.get(pk=User.objects.get(username=self.request.user).persona.vocero.zona.pk))
        return vocero.zona.vivienda_set.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        contexto = super(ViviendaList, self).get_context_data(**kwargs)

        contexto['vocero'] = Vocero.objects.get(persona=self.request.user)

        contexto['cantidadMiembroHogar'] = Miembrohogar.objects.filter(
            hogar__in=Hogar.objects.filter(vivienda__in=contexto['vocero'].zona.vivienda_set.all())).count()

        return contexto


###################################################################################################
@login_required
def vivienda(request, idVivienda=None, idZona=None):
    contexto = {}  # Diccionario de contexto para la plantilla
    contexto['vivienda'] = idVivienda
    contexto['zona'] = idZona
    if contexto['vivienda'] == None:
        contexto['form'] = ViviendaForm()
        active = 'Añadir vivienda'
    else:
        contexto['vivienda'] = Vivienda.objects.get(pk=idVivienda)
        contexto['form'] = ViviendaForm(instance=vivienda)
        contexto['zona'] = vivienda.zona.pk
        contexto['active'] = 'Editar vivienda'

    if request.method == 'POST':
        if contexto['vivienda'] == None:
            contexto['form'] = ViviendaForm(request.POST)
        else:
            contexto['form'] = ViviendaForm(request.POST, instance=contexto['vivienda'])

        if contexto['form'].is_valid():
            contexto['form'].save()
            return HttpResponseRedirect(reverse('zona'))

    return render(request, 'demografia/editarVivienda.html', contexto)


###################################################################################################
@login_required
def eliminarVivienda(request, idVivienda=None):
    vivienda = Vivienda.objects.get(pk=idVivienda)
    if request.method == 'POST':
        vivienda.delete()
        return HttpResponseRedirect(reverse('zona'))
    return render(request, 'demografia/eliminarVivienda.html', {'vivienda': vivienda})


###################################################################################################
@login_required
def ubicacion(request):
    contexto = {}  # Diccionario de contexto para la plantilla
    """
    Esta vista utiliza la API de OpenStreetMap y el framenwork JS Leaftlet para pintar un punto con
    la ubicación de la comunidad
    """
    # Determino la comunidad a la que pertenece el vocero que acaba de logearse.
    contexto['comunidad'] = Vocero.objects.get(persona=request.user).zona.comunidad

    return render(request, 'demografia/ubicacion.html', contexto)


###################################################################################################
@login_required
def mapa(request):
    contexto = {}  # Diccionario de contexto para la plantilla
    """
    Esta vista utiliza la API de OpenStreetMap y el framenwork JS Leaftlet para pintar la poligonal
    de la comunidad
    """
    # Determino la comunidad a la que pertenece el vocero que acaba de logearse.
    contexto['comunidad'] = Vocero.objects.get(persona=request.user).zona.comunidad

    contexto['poligono'] = contexto['comunidad'].poligonal.split()

    return render(request, 'demografia/mapa.html', contexto)


###################################################################################################
@login_required
def comunidad(request):
    """
    Esta vista controla el resumen de la comunidad
    """
    contexto = {}  # Diccionario de contexto para la plantilla
    contexto['vocero'] = Vocero.objects.get(persona=request.user)

    contexto['voceros'] = Vocero.objects.filter(
        zona__in=contexto['vocero'].zona.comunidad.zona_set.all()).order_by('zona', 'persona')

    # Ahora cuento cuantas personas hay en todos los hogares o familias que
    # habitan en las viviendas del conse comunal
    contexto['cantidadMiembroHogar'] = Miembrohogar.objects.filter(
        hogar__in=contexto['vocero'].zona.comunidad.hogar_set.all()).count()

    return render(request, 'demografia/comunidad.html', contexto)


def resumenCenso(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="RESULTADOS_DEL_CENSO_COMUNITARIO_I.pdf"'
    usuario = request.user.username
    buffer = BytesIO()

    report = misReportes(buffer, 'Letter')
    pdf = report.print_users(usuario)

    response.write(pdf)
    return response
