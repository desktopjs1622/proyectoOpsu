"""Ruta para la aplicación del Libro de Oportunidades de Estudio Universitaria
"""
# Librerias Django
from django.urls import path, reverse_lazy
from django.views.generic import DetailView, ListView

# Librerias de terceros
from oeuconfig.models import (
    ActividadCultural, AgrupacionCivica, AyudaEconomica, DisciplinaDeportiva,
    InstanciaAdministrativa, Modalidad, OrganizacionEstudiantil, RedSocial,
    RequisitoIngreso, Servicio, SoporteFormalCambio, TipoCarrera,
    TipoLocalidad, TipoSoporteFormalCambio, TipoTurnoDeEstudio, Titulo)
from oeuconfig.views import (
    AgregarModeloSimple, AgregarSfc, EditarModeloSimple, EditarSfc,
    EliminarInstanciaAdministrativa, EliminarModeloSimple)

# Librerias desarrolladas por mi
from oeu.models import (
    ActividadCulturalLocalidad, AgrupacionCivicaLocalidad,
    AyudaEconomicaLocalidad, DisciplinaDeportivaLocalidad,
    OrganizacionEstudiantilLocalidad, RedSocialLocalidad)

app_name = 'oeuconfig'

urlpatterns = [
    # ############### rutas de los tipos de ayuda económica ##################
    path(  # Listar
        'ieu/tipo-ayuda-economica',
        ListView.as_view(
            model=AyudaEconomica,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Ayuda Económica'}
        ),
        name='listar-tipo-ayuda-economica'),
    path(  # Detalle
        'ieu/tipo-ayuda-economica/detalle/<int:pk>',
        DetailView.as_view(
            model=AyudaEconomica,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Ayuda Económica'}
        ),
        name='detalle-tipo-ayuda-economica'),
    path(  # Agregar
        'ieu/tipo-ayuda-economica/agregar',
        AgregarModeloSimple.as_view(
            model=AyudaEconomica,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-ayuda-economica'),
            success_message='¡El tipo de ayuda económica se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Ayuda Económica'}
        ),
        name='agregar-tipo-ayuda-economica'),
    path(  # Editar
        'ieu/tipo-ayuda-economica/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=AyudaEconomica,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-ayuda-economica'),
            success_message='¡El tipo de ayuda económica se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Ayuda Económica'}
        ),
        name='editar-tipo-ayuda-economica'),
    path(  # Eliminar
        'ieu/tipo-ayuda-economica/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=AyudaEconomica,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfigeu:listar-tipo-ayuda-economica'),
            relacion=AyudaEconomicaLocalidad,
            relacion_id='ayuda_economica_id',
            success_message='¡El tipo de ayuda económica se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Ayuda Económica'}
        ),
        name='eliminar-tipo-ayuda-economica'),

    # ######### rutas de los tipos de actividades culturales #################
    path(  # Listar
        'ieu/tipo-actividades-culturales',
        ListView.as_view(
            model=ActividadCultural,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Actividad Cultural'}
        ),
        name='listar-tipo-actividad-cultural'),
    path(  # Detalle
        'ieu/tipo-actividades-culturales/detalle/<int:pk>',
        DetailView.as_view(
            model=ActividadCultural,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Actividad Cultural'}
        ),
        name='detalle-tipo-actividad-cultural'),
    path(  # Agregar
        'ieu/tipo-actividades-culturales/agregar',
        AgregarModeloSimple.as_view(
            model=ActividadCultural,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-actividad-cultural'),
            success_message='¡El tipo actividad cultural se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Actividad Cultural'}
        ),
        name='agregar-tipo-actividad-cultural'),
    path(  # Editar
        'ieu/tipo-actividades-culturales/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=ActividadCultural,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-actividad-cultural'),
            success_message='¡El tipo actividad cultural se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Actividad Cultural'}
        ),
        name='editar-tipo-actividad-cultural'),
    path(  # Eliminar
        'ieu/tipo-actividades-culturales/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=ActividadCultural,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-actividad-cultural'),
            relacion=ActividadCulturalLocalidad,
            relacion_id='id_actividad_cultural_id',
            success_message='¡El tipo de actividad cultural se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Actividad Cultural'}
        ),
        name='eliminar-tipo-actividad cultural'),

    # ######### rutas de los tipos de disciplina deportiva ###################
    path(  # Listar
        'ieu/tipo-disciplina-deportiva',
        ListView.as_view(
            model=DisciplinaDeportiva,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Disciplina Deportiva'}
        ),
        name='listar-tipo-disciplina-deportiva'),
    path(  # Detalle
        'ieu/tipo-disciplina-deportiva/detalle/<int:pk>',
        DetailView.as_view(
            model=DisciplinaDeportiva,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Disciplina Deportiva'}
        ),
        name='detalle-tipo-disciplina-deportiva'),
    path(  # Agregar
        'ieu/tipo-disciplina-deportiva/agregar',
        AgregarModeloSimple.as_view(
            model=DisciplinaDeportiva,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-disciplina-deportiva'),
            success_message='¡El tipo disciplina deportiva se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Disciplina Deportiva'}
        ),
        name='agregar-tipo-disciplina-deportiva'),
    path(  # Editar
        'ieu/tipo-disciplina-deportiva/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=DisciplinaDeportiva,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-disciplina-deportiva'),
            success_message='¡El tipo disciplina deportiva se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Disciplina Deportiva'}
        ),
        name='editar-tipo-disciplina-deportiva'),
    path(  # Eliminar
        'ieu/tipo-disciplina-deportiva/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=DisciplinaDeportiva,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-disciplina-deportiva'),
            relacion=DisciplinaDeportivaLocalidad,
            relacion_id='disciplina_deportiva_id',
            success_message='¡El tipo de disciplina deportiva se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Disciplina Deportiva'}
        ),
        name='eliminar-tipo-disciplina-deportiva'),

    # ####### rutas de los tipos de organización estudiantil ##################
    path(  # Listar
        'ieu/tipo-organizacion-estudiantil',
        ListView.as_view(
            model=OrganizacionEstudiantil,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Organización Estudiantil'}
        ),
        name='listar-tipo-organizacion-estudiantil'),
    path(  # Detalle
        'ieu/tipo-organizacion-estudiantil/detalle/<int:pk>',
        DetailView.as_view(
            model=OrganizacionEstudiantil,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Organización Estudiantil'}
        ),
        name='detalle-tipo-organizacion-estudiantil'),
    path(  # Agregar
        'ieu/tipo-organizacion-estudiantil/agregar',
        AgregarModeloSimple.as_view(
            model=OrganizacionEstudiantil,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeu:listar-tipo-organizacion-estudiantil'),
            success_message='¡El tipo organización estudiantil se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Organización Estudiantil'}
        ),
        name='agregar-tipo-organizacion-estudiantil'),
    path(  # Editar
        'ieu/tipo-organizacion-estudiantil/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=OrganizacionEstudiantil,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-organizacion-estudiantil'),
            success_message='¡El tipo organización estudiantil se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Organización Estudiantil'}
        ),
        name='editar-tipo-organizacion-estudiantil'),
    path(  # Eliminar
        'ieu/tipo-organizacion-estudiantil/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=OrganizacionEstudiantil,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-organizacion-estudiantil'),
            relacion=OrganizacionEstudiantilLocalidad,
            relacion_id='organizacion_estudiantil_id',
            success_message='¡El tipo de organización estudiantil se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Organización Estudiantil'}
        ),
        name='eliminar-tipo-organizacion-estudiantil'),

    # ########## rutas de los tipos de agrupación cívica #####################
    path(  # Listar
        'ieu/tipo-agrupacion-civica',
        ListView.as_view(
            model=AgrupacionCivica,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Agrupación Cívica'}
        ),
        name='listar-tipo-agrupacion-civica'),
    path(  # Detalle
        'ieu/tipo-agrupacion-civica/detalle/<int:pk>',
        DetailView.as_view(
            model=AgrupacionCivica,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Agrupación Cívica'}
        ),
        name='detalle-tipo-agrupacion-civica'),
    path(  # Agregar
        'ieu/tipo-agrupacion-civica/agregar',
        AgregarModeloSimple.as_view(
            model=AgrupacionCivica,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-agrupacion-civica'),
            success_message='¡El tipo agrupación cívica se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Agrupación Cívica'}
        ),
        name='agregar-tipo-agrupacion-civica'),
    path(  # Editar
        'ieu/tipo-agrupacion-civica/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=AgrupacionCivica,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-agrupacion-civica'),
            success_message='¡El tipo agrupación cívica se actualizó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Agrupación Cívica'}
        ),
        name='editar-tipo-agrupacion-civica'),
    path(  # Eliminar
        'ieu/tipo-agrupacion-civica/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=AgrupacionCivica,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeu:listar-tipo-agrupacion-civica'),
            relacion=AgrupacionCivicaLocalidad,
            relacion_id='agrupacion_civica_id',
            success_message='¡El tipo de agrupación cívica se eliminó' '\n' 
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Agrupación Cívica'}
        ),
        name='eliminar-tipo-agrupacion-civica'),

    # ############ rutas de los tipos de redes sociales #######################
    path(  # Listar
        'ieu/tipo-redes-sociales',
        ListView.as_view(
            model=RedSocial,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Redes Sociales'}
        ),
        name='listar-tipo-redes-sociales'),
    path(  # Detalle
        'ieu/tipo-redes-sociales/detalle/<int:pk>',
        DetailView.as_view(
            model=RedSocial,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Redes Sociales'}
        ),
        name='detalle-tipo-redes-sociales'),
    path(  # Agregar
        'ieu/tipo-redes-sociales/agregar',
        AgregarModeloSimple.as_view(
            model=RedSocial,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-redes-sociales'),
            success_message='¡El tipo red social se agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo Redes Sociales'}
        ),
        name='agregar-tipo-redes-sociales'),
    path(  # Editar
        'ieu/tipo-redes-sociales/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=RedSocial,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-redes-sociales'),
            success_message='¡El tipo red social se actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo Redes Sociales'}
        ),
        name='editar-tipo-redes-sociales'),
    path(  # Eliminar
        'ieu/tipo-redes-sociales/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=RedSocial,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-redes-sociales'),
            relacion=RedSocialLocalidad,
            relacion_id='red_social_id',
            success_message='¡El tipo de red social se eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo Redes Sociales'}
        ),
        name='eliminar-tipo-redes-sociales'),

    # ################### rutas de los tipos de localidad #####################
    path(  # Listar
        'ieu/tipo-de-localidad',
        ListView.as_view(
            model=TipoLocalidad,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo de Localidad'}
        ),
        name='listar-tipo-de-localidad'),
    path(  # Detalle
        'ieu/tipo-de-localidad/detalle/<int:pk>',
        DetailView.as_view(
            model=TipoLocalidad,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo de Localidad'}
        ),
        name='detalle-tipo-de-localidad'),
    path(  # Agregar
        'ieu/tipo-de-localidad/agregar',
        AgregarModeloSimple.as_view(
            model=TipoLocalidad,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-localidad'),
            success_message='¡El tipo de localidad se agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Localidad'}
        ),
        name='agregar-tipo-de-localidad'),
    path(  # Editar
        'ieu/tipo-de-localidad/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=TipoLocalidad,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-localidad'),
            success_message='¡El tipo de localidad se actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Localidad'}
        ),
        name='editar-tipo-de-localidad'),
    path(  # Eliminar
        'ieu/tipo-de-localidad/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=TipoLocalidad,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-localidad'),
            success_message='¡El tipo de localidad se eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Localidad'}
        ),
        name='eliminar-tipo-de-localidad'),

    # ############## rutas de los tipos de requisito de ingreso ###############
    path(  # Listar
        'ieu/tipo-de-requisito-de-ingreso',
        ListView.as_view(
            model=RequisitoIngreso,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Requisito de Ingreso'}
        ),
        name='listar-tipo-de-requisito-ingreso'),
    path(  # Detalle
        'ieu/tipo-de-requisito-de-ingreso/detalle/<int:pk>',
        DetailView.as_view(
            model=RequisitoIngreso,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Requisito de Ingreso'}
        ),
        name='detalle-tipo-de-requisito-ingreso'),
    path(  # Agregar
        'ieu/tipo-de-requisito-de-ingreso/agregar',
        AgregarModeloSimple.as_view(
            model=RequisitoIngreso,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-requisito-ingreso'),
            success_message='¡El tipo requisito de ingreso se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Requisito de Ingreso'}
        ),
        name='agregar-tipo-de-requisito-ingreso'),
    path(  # Editar
        'ieu/tipo-de-requisito-de-ingreso/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=RequisitoIngreso,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-requisito-ingreso'),
            success_message='¡El tipo requisito de ingreso se actualizó' '\n' 
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Requisito de Ingreso'}
        ),
        name='editar-tipo-de-requisito-ingreso'),
    path(  # Eliminar
        'ieu/tipo-de-requisito-de-ingreso/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=RequisitoIngreso,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-requisito-ingreso'),
            success_message='¡El tipo turno de estudio se eliminó de' '\n' 
                            'manera exitosa!',
            extra_context={'titulo': 'Tipo Requisito de Ingreso'}
        ),
        name='eliminar-tipo-de-requisito-ingreso'),

    # ########### rutas de los tipos de soporte form. de cambio ##############
    path(  # Listar
        'tipo-de-soporte-formal-de-cambio',
        ListView.as_view(
            model=TipoSoporteFormalCambio,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo Soporte Formal de Cambio'}
        ),
        name='listar-tipo-sfc'),
    path(  # Detalle
        'tipo-de-soporte-formal-de-cambio/detalle/<int:pk>',
        DetailView.as_view(
            model=TipoSoporteFormalCambio,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Soporte Formal de Cambio'}
        ),
        name='detalle-tipo-sfc'),
    path(  # Agregar
        'tipo-de-soporte-formal-de-cambio/agregar',
        AgregarModeloSimple.as_view(
            model=TipoSoporteFormalCambio,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-sfc'),
            success_message='¡El tipo de soporte formal de cambio se' '\n'
                            'agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo Soporte Formal de Cambio'}
        ),
        name='agregar-tipo-sfc'),
    path(  # Editar
        'tipo-de-soporte-formal-de-cambio/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=TipoSoporteFormalCambio,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-sfc'),
            success_message='¡El tipo de soporte formal de cambio se' '\n' 
                            'actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo Soporte Formal de Cambio'}
        ),
        name='editar-tipo-sfc'),
    path(  # Eliminar
        'tipo-de-soporte-formal-de-cambio/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=TipoSoporteFormalCambio,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-sfc'),
            success_message='¡El tipo de soporte formal de cambio se' '\n'
                            'eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo Soporte Formal de Cambio'}
        ),
        name='eliminar-tipo-sfc'),

    # ################# rutas de los tipos de modalidad #####################
    path(  # Listar
        'pfa/tipo-de-modalidad',
        ListView.as_view(
            model=Modalidad,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo de Modalidad'}
        ),
        name='listar-tipo-de-modalidad'),
    path(  # Detalle
        'pfa/tipo-de-modalidad/detalle/<int:pk>',
        DetailView.as_view(
            model=Modalidad,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo de Modalidad'}
        ),
        name='detalle-tipo-de-modalidad'),
    path(  # Agregar
        'pfa/tipo-de-modalidad/agregar',
        AgregarModeloSimple.as_view(
            model=Modalidad,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-modalidad'),
            success_message='¡El tipo de modalidad se agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Modalidad'}
        ),
        name='agregar-tipo-de-modalidad'),
    path(  # Editar
        'pfa/tipo-de-modalidad/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=Modalidad,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-modalidad'),
            success_message='¡El tipo de modalidad se actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Modalidad'}
        ),
        name='editar-tipo-de-modalidad'),
    path(  # Eliminar
        'pfa/tipo-de-modalidad/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=Modalidad,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-de-modalidad'),
            success_message='¡El tipo de modalidad se eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Modalidad'}
        ),
        name='eliminar-tipo-de-modalidad'),


    # ################# rutas de los tipos de título #########################
    path(  # Listar
        'pfa/tipo-de-titulo',
        ListView.as_view(
            model=Titulo,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo de Título'}
        ),
        name='listar-tipo-titulo'),
    path(  # Detalle
        'pfa/tipo-de-titulo/detalle/<int:pk>',
        DetailView.as_view(
            model=Titulo,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo de Título'}
        ),
        name='detalle-tipo-titulo'),
    path(  # Agregar
        'pfa/tipo-de-titulo/agregar',
        AgregarModeloSimple.as_view(
            model=Titulo,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-titulo'),
            success_message='¡El tipo de título se agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Título'}
        ),
        name='agregar-tipo-titulo'),
    path(  # Editar
        'pfa/tipo-de-titulo/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=Titulo,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-titulo'),
            success_message='¡El tipo de título se actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Título'}
        ),
        name='editar-tipo-titulo'),
    path(  # Eliminar
        'pfa/tipo-de-titulo/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=Titulo,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-titulo'),
            success_message='¡El tipo de título se eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Título'}
        ),
        name='eliminar-tipo-titulo'),


    # ################# rutas de los tipos de carrera #########################
    path(  # Listar
        'pfa/tipo-de-carrera',
        ListView.as_view(
            model=TipoCarrera,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo de Carrera'}
        ),
        name='listar-tipo-carrera'),
    path(  # Detalle
        'pfa/tipo-de-carrera/detalle/<int:pk>',
        DetailView.as_view(
            model=TipoCarrera,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo de Carrera'}
        ),
        name='detalle-tipo-carrera'),
    path(  # Agregar
        'pfa/tipo-de-carrera/agregar',
        AgregarModeloSimple.as_view(
            model=TipoCarrera,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfigoeu:listar-tipo-titulo'),
            success_message='¡El tipo de carrera se agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Carrera'}
        ),
        name='agregar-tipo-carrera'),
    path(  # Editar
        'pfa/tipo-de-carrera/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=TipoCarrera,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-carrera'),
            success_message='¡El tipo de carrera se actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Carrera'}
        ),
        name='editar-tipo-carrera'),
    path(  # Eliminar
        'pfa/tipo-de-carrera/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=TipoCarrera,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-carrera'),
            success_message='¡El tipo de carrera se eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Carrera'}
        ),
        name='eliminar-tipo-carrera'),

    # ################# rutas de los tipos de servicio #########################
    path(  # Listar
        'ieu/tipo-de-servicio',
        ListView.as_view(
            model=Servicio,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Tipo de Servicio'}
        ),
        name='listar-tipo-servicio'),
    path(  # Detalle
        'ieu/tipo-de-servicio/detalle/<int:pk>',
        DetailView.as_view(
            model=Servicio,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo de Servicio'}
        ),
        name='detalle-tipo-servicio'),
    path(  # Agregar
        'ieu/tipo-de-servicio/agregar',
        AgregarModeloSimple.as_view(
            model=Servicio,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-servicio'),
            success_message='¡El tipo de servicio se agregó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Servicio'}
        ),
        name='agregar-tipo-servicio'),
    path(  # Editar
        'ieu/tipo-de-servicio/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=Servicio,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-servicio'),
            success_message='¡El tipo de servicio se actualizó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Servicio'}
        ),
        name='editar-tipo-servicio'),
    path(  # Eliminar
        'ieu/tipo-de-servicio/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=Servicio,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-servicio'),
            success_message='¡El tipo de servicio se eliminó de manera exitosa!',
            extra_context={'titulo': 'Tipo de Servicio'}
        ),
        name='eliminar-tipo-servicio'),


    # ################### rutas de los tipos de turnos #######################
    path(  # Listar
        'pfa/tipo-turno-de-estudio',
        ListView.as_view(
            model=TipoTurnoDeEstudio,
            template_name='modelo_simple_listar.html',
            extra_context={'titulo': 'Turnos de Estudios'}
        ),
        name='listar-tipo-turno-de-estudio'), #ruta para el archivo de menu_lateral
    path(  # Detalle
        'pfa/tipo-turno-de-estudio/detalle/<int:pk>',
        DetailView.as_view(
            model=TipoTurnoDeEstudio,
            template_name='modelo_simple_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Turnos de Estudios'}
        ),
        name='detalle-tipo-turno-de-estudio'),
    path(  # Agregar
        'pfa/tipo-turno-de-estudio/agregar',
        AgregarModeloSimple.as_view(
            model=TipoTurnoDeEstudio,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-turno-de-estudio'),
            success_message='¡El tipo turno de estudio se agregó de manera' '\n'
                            'exitosa!',
            extra_context={'titulo': 'Tipo Turnos de Estudios'}
        ),
        name='agregar-tipo-turno-de-estudio'),
    path(  # Editar
        'pfa/tipo-turno-de-estudio/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=TipoTurnoDeEstudio,
            fields=['nombre', 'descripcion'],
            template_name='modelo_simple_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-turno-de-estudio'),
            success_message='¡El tipo turno de estudio se actualizó de manera' '\n' 
                            'exitosa!',
            extra_context={'titulo': 'Tipo Turnos de Estudios'}
        ),
        name='editar-tipo-turno-de-estudio'),
    path(  # Eliminar
        'pfa/tipo-turno-de-estudio/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=TipoTurnoDeEstudio,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-tipo-turno-de-estudio'),
            success_message='¡El tipo turno de estudio se eliminó de manera' '\n'
                            'exitosa!',
            extra_context={'titulo': 'Tipo Turnos de Estudios'}
        ),
        name='eliminar-tipo-turno-de-estudio'),


    # ########## rutas el modulo de instancia administrativa ###################
    path(  # Listar
        'ieu/tipo-de-instancia-administrativa',
        ListView.as_view(
            model=InstanciaAdministrativa,
            template_name='tipo_instancia_administrativa_listar.html',
            extra_context={'titulo': 'Instancia Administrativa'}
        ),
        name='listar-instancia-administrativa'),
    path(  # Detalle
        'ieu/tipo-de-instancia-administrativa/detalle/<int:pk>',
        DetailView.as_view(
            model=InstanciaAdministrativa,
            template_name='tipo_instancia_administrativa_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Tipo Instancia Administrativa'}
        ),
        name='detalle-tipo-instancia-administrativa'),
    path(  # Agregar
        'ieu/tipo-de-instancia-administrativa/agregar',
        AgregarModeloSimple.as_view(
            model=InstanciaAdministrativa,
            fields=['nombre', 'publicar'],
            template_name='tipo_instancia_administrativa_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-instancia-administrativa'),
            success_message='¡El tipo de instancia administrativa se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Instancia Administrativa'}
        ),
        name='agregar-tipo-instancia-administrativa'),
    path(  # Editar
        'ieu/tipo-de-instancia-administrativa/editar/<int:pk>',
        EditarModeloSimple.as_view(
            model=InstanciaAdministrativa,
            fields=['nombre', 'publicar'],
            template_name='tipo_instancia_administrativa_formulario.html',
            success_url=reverse_lazy('oeuconfig:listar-instancia-administrativa'),
            success_message='¡El tipo de instancia administrativa se actualizó' '\n' 
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Instancia Administrativa'}
        ),
        name='editar-tipo-instancia-administrativa'),
    path(  # Eliminar
        'ieu/tipo-de-instancia-administrativa/eliminar/<int:pk>',
        EliminarInstanciaAdministrativa.as_view(
            model=InstanciaAdministrativa,
            template_name='modelo_simple_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-instancia-administrativa'),
            success_message='¡El tipo de instancia administrativa se eliminó' '\n' 
                            'de manera exitosa!',
            extra_context={'titulo': 'Tipo Instancia Administrativa'}
        ),
        name='eliminar-tipo-instancia-administrativa'),


    # ########## rutas el modulo Soporte Formal de Cambio ###################
    path(  # Listar
        'soporte-formal-de-cambio',
        ListView.as_view(
            model=SoporteFormalCambio,
            template_name='soporte_formal_cambio_listar.html',
            extra_context={'titulo': 'Soporte Formal de Cambio'}
        ),
        name='listar-soporte-formal-cambio'),
    path(  # Detalle
        'soporte-formal-de-cambio/detalle/<int:pk>',
        DetailView.as_view(
            model=SoporteFormalCambio,
            template_name='soporte_formal_cambio_detalle.html',
            context_object_name='detalle',
            extra_context={'titulo': 'Soporte Formal de Cambio'}
        ),
        name='detalle-soporte-formal-cambio'),
    path(  # Agregar
        'soporte-formal-de-cambio/agregar',
        AgregarSfc.as_view(
            success_message='¡El soporte formal de cambio se agregó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Soporte Formal de Cambio'}
        ),
        name='agregar-soporte-formal-cambio'),
    path(  # Editar
        'soporte-formal-de-cambio/editar/<int:pk>',
        EditarSfc.as_view(
            success_message='¡El soporte formal de cambio se actualizó' '\n' 
                            'de manera exitosa!',
            extra_context={'titulo': 'Soporte Formal de Cambio'}
        ),
        name='editar-soporte-formal-cambio'),
    path(  # Eliminar
        'soporte-formal-de-cambio/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=SoporteFormalCambio,
            template_name='soporte_formal_cambio_eliminar.html',
            success_url=reverse_lazy('oeuconfig:listar-soporte-formal-cambio'),
            success_message='¡El soporte formal de cambio se eliminó' '\n'
                            'de manera exitosa!',
            extra_context={'titulo': 'Soporte Formal de Cambio'}
        ),
        name='eliminar-soporte-formal-cambio'),
]
