# Librerias Standard
import time

# Librerias Django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg, Count, Max, Min, Sum
from django.http import (
    Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import loader
from django.urls import reverse, reverse_lazy
# MANEJO DE FECHAS
from django.utils import timezone
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView)
from django.views.generic.edit import DeletionMixin

# Librerias de terceros
from cuenta.models import Persona
from dal import autocomplete

# Librerias desarrolladas por mi
from globales.models import Saime

# Librerias en carpetas locales
from .forms import ActogradoForm, GraduandoForm
from .metodos import date, qs, qs404
from .models import Actogrado, Graduando, LocalidadPersona

# Create your views here.

###############################################################################################
########################################  INDEX    ############################################
###############################################################################################


class ListarActo(ListView):
    template_name = 'actos/list.html'
    extra_context = {'titulo':'Actos de Grado',
                    'sub_titulo':'Actos de Grado en las IEU'}
    context_object_name = 'actos'
    
    def get_queryset(self):
        """ Definicion de mis variables globales """
        global responsable_ieu, acto
        num = None
        
        responsable_ieu = LocalidadPersona.objects.get(persona = self.request.user.pk)
        acto = qs(Actogrado, **{'localidad':responsable_ieu.localidad})
        return acto
    
        
    def get_context_data(self, **kwargs):
        contexto = super(ListarActo, self).get_context_data(**kwargs)
        contexto['fecha'] = date('formateada')
        contexto['annio_actual'] = date('year')
        contexto['annio_anterior'] = date('last_year')
        contexto['general'] = 'general'
        contexto['num'] = self.num = 1
        contexto['mi_localidad'] = responsable_ieu.localidad
        contexto['actos_totales'] = acto.count()
        contexto['num_actos_abiertos'] = acto.filter(status = True, fecha_acto__year = date('year')).count()
 
        contexto['graduando_annio_pasado'] = qs(Graduando,**{'actogrado__fecha_acto__year':date('last_year'),
                                                            'actogrado__localidad':responsable_ieu.localidad,
                                                            'actogrado__responsable':self.request.user}).count()
        contexto['graduandos_actuales'] = qs(Graduando,**{'actogrado__fecha_acto__year':date('year'),
                                                        'actogrado__localidad':responsable_ieu.localidad,
                                                        'actogrado__responsable':self.request.user}).count()
        contexto['graduandos_generales'] = qs(Graduando,**{'actogrado__localidad':responsable_ieu.localidad}).count()
        return contexto
    
    def prueba(self):
        x = self.get_context_data(self, **kwargs)
        return self.num

class GenerarActo(SuccessMessageMixin,CreateView):
    model = Actogrado
    template_name = 'actos/modal_create_acto.html'
    form_class = ActogradoForm
    success_url = reverse_lazy('grado:act_list')
    success_messages = 'Se ha guardado exitosamente el acto de grado'
    extra_context = {'titulo':'Actos de Grado',
                    'sub_titulo':'Actos de Grado en las IEU'}

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        responsable_ieu = LocalidadPersona.objects.get(persona = self.request.user.pk)
        
        if qs(Actogrado, **{'status':True, 'localidad':responsable_ieu.localidad}).count() == 0:
            if form.is_valid():
                acto = form.save(commit = False)
                acto.localidad = responsable_ieu.localidad
                acto.num_acta = Actogrado.objects.filter(
                                                localidad = acto.localidad
                                                ).latest('num_acta').num_acta + 1
                acto.responsable = self.request.user
                return self.form_valid(form)
        else:
            messages.error(request, 'No se pueden aperturar nuevos actos de grado\
                                    mientras en anterior se encuentre abierto!')
            return HttpResponseRedirect(self.get_success_url())

class EditarActo(UpdateView):
    model = Actogrado
    form_class = ActogradoForm
    template_name = 'actos/modal_create_acto.html'
    success_url = reverse_lazy('grado:act_list')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.form_class(request.POST, instance = self.object)
        if form.is_valid():
            acto = form.save(commit = False)
            if acto.status == True:
                messages.success(request, 'Modificación exitosa del acto de grado')
                return self.form_valid(form)
            else:
                messages.warning(request, 'Usted no puede modificar un acto de grado con status cerrado')
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, 'No se ha logrado completar la modificación del acto de grado')
            return HttpResponseRedirect(self.get_success_url())


class CerrarActo(UpdateView):
    model = Actogrado
    template_name = 'actos/cerrar_acto.html'
    fields = ['status'] 
    success_url = reverse_lazy('grado:act_list')
    extra_context = {'titulo':'Usted va cerrar el acto de grado con nro. de acta',
                    'tag':'danger',
                    'label':'check',
                    }

    def get_context_data(self, **kwargs):
        contexto = super(CerrarActo, self).get_context_data(**kwargs)
        contexto['participantes'] = Graduando.objects.filter(actogrado = self.get_object())
        return contexto
                    
    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == True:
            self.object.status = False
            """ Aquí debo colocar la funcion foliar """
            self.object.save()
            messages.success(request,'El acto de grado ha sido cerrado')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request,'No se ha podido cerrar el acto de grado')
            return HttpResponseRedirect(self.get_success_url())


class EliminarActo(CerrarActo,DeleteView):
    model = Actogrado
    template_name = 'actos/eliminar_acto.html'
    success_url = reverse_lazy('grado:act_list')
    extra_context = {'titulo':'Eliminar el acto de grado con acta nro. ', 'label':'trash','tag':'danger'}
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == False:

            messages.warning(request, 'Usted no puede eliminar un acto de grado con status cerrado.')
            return HttpResponseRedirect(self.get_success_url())
        elif not self.request.user.is_superuser:
            messages.error(request, 'Usted no tiene los permisos necesarios para realizar esta acción')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.success(request, 'Acto eliminado de manera satisfactoria')
            return self.delete(request, *args, **kwargs)


##########################################################


class ListGraduando(DetailView):
    model = Actogrado
    template_name = 'graduandos/list.html'
    
    
    def get_context_data(self, **kwargs):
        contexto = super(ListGraduando, self).get_context_data(**kwargs)
        contexto['graduandos'] = Graduando.objects.filter(actogrado = self.kwargs['pk'])
        contexto['graduandos_inscritos_count'] = contexto['graduandos'].count() 
        contexto['titulo'] = 'Listado de Graduandos'
        contexto['sub_titulo'] = 'Detalles del Acto'
        contexto['fecha'] = date('formateada')
        contexto['class_inst'] = ListarActo
        return contexto

class DetailGraduando(DetailView):
    model = Graduando
    template_name = 'graduandos/modal_detalle_graduando.html'
    

class CreateGraduando(CreateView):
    model = Graduando
    form_class = GraduandoForm
    template_name = 'graduandos/modal_create_graduando.html'
    extra_context = {'titulo':'Inscripción de graduando','boton':'Guardar','accion':'save'}

    def get_context_data(self, **kwargs):
        contexto = super(CreateGraduando, self).get_context_data(**kwargs)
        """ Definicion de mis variables globales """
        global responsable_ieu, acto
        responsable_ieu = LocalidadPersona.objects.get(persona = self.request.user.pk)
        acto = Actogrado.objects.get(id = self.kwargs['pk'],\
                                    localidad = responsable_ieu.localidad)
        """ Aquí paso el acto de grado al cual se va inscribir al nuevo graduando """
        contexto['pk'] = acto.pk
        return contexto

        
    def get_success_url(self, **kwargs):
        return reverse_lazy('grado:grad_list', kwargs = {'pk':self.kwargs['pk']})
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)        
        """ HACER LAS VALIDACIONES PARA QUE UN USUARIO NO SE PUEDA REGISTRAR SI YA ESTA REGISTRADO """
        if acto.status == True:
            """ Si el acto esta abierto procede a validar los datos suministrados """
            if form.is_valid():
                graduando = form.save(commit = False)
                graduando.actogrado = acto
                graduando.responsable = self.request.user
                # if graduando.persona == None:
                #     messages.info(request, 'El número de cedula es requerido para completar el registro!')
                #     return HttpResponseRedirect(self.get_success_url())
                # elif graduando.carrera == None:
                #     messages.info(request, 'La carrera es requerida para completar el registro!')
                #     return HttpResponseRedirect(self.get_success_url())
                # else:
                messages.success(request,'Graduando registrado satisfactoriamente!')
                return self.form_valid(form)
            else:
                messages.error(request, 'Ha ocurrido un error al momento de registrar al nuevo graduando')
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.warning(request, 'Acto de grado cerrado, NO se pueden registrar nuevos graduandos.')
            return HttpResponseRedirect(self.get_success_url())


class UpdateGraduando(UpdateView):
    model = Graduando
    form_class = GraduandoForm
    template_name = 'graduandos/modal_create_graduando.html'
    extra_context = {'titulo':'Edición del graduando','boton':'Guardar','accion':'save'}

    def get_success_url(self, **kwargs):
        return reverse_lazy('grado:grad_list', kwargs = {'pk':self.kwargs['acto']})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance = self.object)
        if self.object.actogrado.status == True:
            if form.is_valid():
                messages.success(request, 'Modificación exitosa')
                return self.form_valid(form)
            else:
                messages.error(request, 'Para realizar modificaciones el acto de grado debe estar abierto')
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.info(request, 'Para modificar las opciones del graduando el acto en el que participa debe estar abierto')
            return HttpResponseRedirect(self.get_success_url())
            

class DeleteGraduando(DeleteView):
    model = Graduando
    template_name = 'graduandos/modal_delete_graduando.html'
    extra_context = {'titulo':'Usted va eliminar los datos de ', 'label':'trash', 'tag':'danger'}

    def get_success_url(self, **kwargs):
        return reverse_lazy('grado:grad_list', kwargs = {'pk':self.kwargs['acto']})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        responsable_ieu = LocalidadPersona.objects.filter(persona = self.request.user.pk)
        if self.object.num_asignado == None:
            messages.success(request, 'Solicitud exitosa!')
            return self.delete(request, *args, **kwargs)
            
        else:
            messages.error(request, 'Este Acto de Grado se encuentra cerrado\
                                    ,no se puede realizar la acción solicitada.')
            return HttpResponseRedirect(self.get_success_url())

##########################################################

###############################################################################################
##################################  AUTOCOMPLETE   ############################################
###############################################################################################


class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        persona = Saime.objects.all()
        if self.q:
                persona = Saime.objects.filter(cedula_identidad=self.q)
        return persona
