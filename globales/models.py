# -*- coding: utf-8
"""
Modelo de datos de la app globales
"""
# Librerias Future
from __future__ import unicode_literals

# Librerias Standard
from datetime import datetime

# Librerias Django
from django.db import models

# from filer.fields.file import FilerFileField


# class Archivo(models.Model):
#     id_archivo = models.AutoField(primary_key=True, db_column='id_archivo')
#     descripcion_archivo = models.TextField(max_length=255, blank=True, null=True)
#     archivo = FilerFileField(blank=True, null=True, verbose_name='Descripción Anexo')

#     def __str__(self):
#         return self.descripcion_archivo

#     class Meta:
#         db_table = 'archivo'
#         verbose_name = "Archivo"
#         verbose_name_plural = "Archivos"


class Pais(models.Model):
    '''Gestión de paises
    '''
    cod_iso = models.CharField(max_length=3, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    nombre_iso = models.CharField(max_length=255, blank=True, null=True)
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    alfa3 = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'pais'


class Estado(models.Model):
    '''Gestión de estados
    '''
    id_estado_ine = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estado'


class Municipio(models.Model):
    '''Gestión de municipios
    '''
    id_municipio_completo_ine = models.CharField(max_length=4)
    id_estado_ine = models.CharField(Estado, max_length=2)
    id_municipio_ine = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'municipio'


class Parroquia(models.Model):
    '''Gestión de parroquias
    '''
    id_parroquia_completo_ine = models.CharField(max_length=6)
    id_municipio_completo_ine = models.CharField(max_length=4)
    id_estado_ine = models.CharField(max_length=2)
    id_municipio_ine = models.CharField(max_length=2)
    id_parroquia_ine = models.CharField(max_length=2)
    nombre = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'parroquia'


class Etnia(models.Model):
    '''Gestión de etnias
    '''
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'etnia'


def consulta_cne():
    """
    Busca la parroquia en la vota la persona
    """
    counter = 0
    counter += 1
    return counter


class Saime(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    letra_cedula_identidad = models.CharField(max_length=1)
    cedula_identidad = models.IntegerField(unique=True)
    rif = models.CharField(max_length=255, blank=True, null=True)
    otros_nombres = models.CharField(max_length=255, blank=True, null=True)
    otros_apellidos = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    pasaporte = models.CharField(max_length=255, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    cne = models.CharField(max_length=255, blank=True, null=True)
    conyuge = models.ForeignKey('Saime', on_delete=models.PROTECT, 
            related_name='conyuges', blank=True, null=True)
    etnia = models.ForeignKey('Saime', on_delete=models.PROTECT, 
            related_name='etnias', blank=True, null=True)
    madre = models.ForeignKey('Saime', on_delete=models.PROTECT, 
            related_name='madres', blank=True, null=True)
    padre = models.ForeignKey('Saime', on_delete=models.PROTECT, 
            related_name='padres', blank=True, null=True)
    pais_nacimiento = models.ForeignKey(Pais, on_delete=models.PROTECT, 
            related_name='paises', blank=True, null=True)
    correo_secundario = models.CharField(max_length=254, blank=True, 
            null=True)

    def __str__(self):
        return '%s %s %s %s' % (self.first_name, self.otros_nombres, self.last_name, self.otros_apellidos)
    
    @property
    def get_short_name(self):
        return '%s  %s' % (self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'saime'


##############################################################################
class InstitucionMinisterial(models.Model):
    """Este modelo sirve para almacenar las Instituciones que dependen del
    MPPEUCT
    """
    TIPO_INSTITUCION_CHOICES = (
        ('IEU', 'INSTITUCIÓN DE EDUCACIÓN UNIVERSITARIA'),
        ('ENTE ADSCRITO', 'ENTE ADSCRITO'),
        ('OTRO', 'OTRO'),
    )
    DEP_ADMIN_CHOICES = (
        ('PÚBLICA', 'PÚBLICA'),
        ('PRIVADA', 'PRIVADA'),
    )
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=50)
    rif = models.CharField(max_length=45)
    dep_admin = models.CharField(max_length=7, choices=DEP_ADMIN_CHOICES)
    tipo_institucion = models.CharField(
        max_length=37,
        choices=TIPO_INSTITUCION_CHOICES
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre', ]
        db_table = 'institucion_ministerial'
        verbose_name = "Ente Adscrito"
        verbose_name_plural = "Entes Adscritos"


##############################################################################
class CorreoInstitucion(models.Model):
    """agregar comentario de la clase
    """
    institucion = models.ForeignKey(
        'InstitucionMinisterial', on_delete=models.PROTECT, db_index=True)
    instancia_administrativa = models.ForeignKey(
        'oeu.InstanciaAdministrativa', on_delete=models.PROTECT, db_index=True)
    correo = models.EmailField(max_length=255)

    class Meta:
        db_table = 'correo_institucion'
        verbose_name = "Correo Institución"
        verbose_name_plural = "Correos Institución"


##############################################################################
class AutoridadesInstitucion(models.Model):
    """Autoridades
    """
    institucion = models.ForeignKey(
        'InstitucionMinisterial', on_delete=models.PROTECT, db_index=True)
    persona = models.ForeignKey(
        'cuenta.Persona', on_delete=models.PROTECT, db_index=True)
    instancia_administrativa = models.ForeignKey(
        'oeu.InstanciaAdministrativa', on_delete=models.PROTECT, db_index=True)
    correo = models.EmailField(max_length=255)
    telefono = models.EmailField(max_length=19)
    celular = models.EmailField(max_length=19)

    class Meta:
        db_table = 'autoridad_institucion'
        verbose_name = "Autoridad Institución"
        verbose_name_plural = "Autoridades Institución"
