# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.db import models
from django.utils import timezone
from django.utils.six import with_metaclass

# Create your models here.

class Clinica(models.Model):
    rif = models.CharField(
        max_length=13,
        db_column='rif',
        verbose_name='rif de la clinica',
        unique=True,
    )
    nombre = models.CharField(
        max_length=255,
        db_column='nombre',
        verbose_name='nombre de la clinica'
    )
    estado = models.ForeignKey(
        'globales.Estado',
        verbose_name='estado de la clinica',
        on_delete=models.PROTECT
    )
    municipio = models.ForeignKey(
        'globales.Municipio',
        verbose_name='municipio de la clinica',
        on_delete=models.PROTECT
    )
    parroquia = models.ForeignKey(
        'globales.Parroquia',
        verbose_name='parroquia de la clinica',
        on_delete=models.PROTECT,
        null = True,
        blank = True,
    )
    direccion = models.TextField()
    editor = models.ForeignKey(
        'cuenta.Persona',
        verbose_name='Editor de la clínica',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return '%s, %s' % (self.rif, self.nombre)

    class Meta:
        db_table = 'sismeu\".\"clinica'
        verbose_name = "Clinica"
        verbose_name_plural = "Clinicas"

#############################################################################
class Departamento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        db_table = 'sismeu\".\"departamento'
        verbose_name = "Departamento de la clínica"
        verbose_name_plural = "Departamentos de la clínica"


#############################################################################
class TelefonoClinica(models.Model):
    """ En este modelo es posible alamcenar los telefonos de los departamentos
    y personas de interes (Gerentes, medicos, dueños, etc.) de la clinica
    """
    clinica = models.ForeignKey(
        'Clinica',
        verbose_name='Clinica a contactar',
        on_delete=models.CASCADE
    )
    departamento = models.ForeignKey(
        'Departamento',
        verbose_name='Departamento',
        on_delete=models.PROTECT
    )
    telefono = models.CharField(
        max_length=30,
        db_column='telefono',
        verbose_name='Telefono de la clinica'
    )
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.departamento)

    class Meta:
        db_table = 'sismeu\".\"telefono_clinica'
        verbose_name = "Telefono de la clínica"
        verbose_name_plural = "Telefonos de la clínica"

#############################################################################
class Convenios(models.Model):
    nombre = models.CharField(
        max_length=30,
        db_column='nombre',
        verbose_name='Nombre del convenio'
    )
    descripcion = models.TextField()

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        db_table = 'sismeu\".\"convenios'
        verbose_name = "Convenio con la clínica"
        verbose_name_plural = "Convenios de la clínica"

#############################################################################
class ConvenioClinica(models.Model):
    clinica = models.ForeignKey(
        'Clinica',
        verbose_name='Clínica del convenio',
        on_delete=models.PROTECT
    )
    convenio = models.ForeignKey(
        'Convenios',
        verbose_name='Convenio con la clínica',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return '%s' % (self.convenio)

    class Meta:
        db_table = 'sismeu\".\"convenio_clinica'
        verbose_name = "Convenio con la clínica"
        verbose_name_plural = "Convenios con la clínica"

#############################################################################
class HistoricoClinica(models.Model):
    clinica = models.ForeignKey(
        'Clinica',
        db_column='clinica_id',
        verbose_name='Clinica',
        on_delete=models.PROTECT
    )
    fecha_activacion = models.DateTimeField(
        verbose_name='fecha de activacion de la clinica',
        auto_now_add=True,
    )
    responsable_activacion = models.ForeignKey(
        'cuenta.Persona',
        related_name='reponsable_regional_id',
        db_column='responsable_activacion',
        verbose_name='responsable de la activacion de la clinica',
        on_delete=models.DO_NOTHING
    )
    motivo_inactivacion = models.ForeignKey(
        'MotivoInactivacion',
        related_name='motivo_inactivacion_id',
        db_column='motivo_inactivacion_id',
        verbose_name='Motivo para inactivar la clinica',
        on_delete=models.PROTECT,
        null=True
    )
    fecha_inactivacion = models.DateField(
        verbose_name='fecha de inactivacion de la clinica',
        null=True,
        )
    responsable_inactivacion = models.ForeignKey(
        'cuenta.Persona',
        related_name='responsable_regional_id',
        db_column='responsable_inactivacion',
        verbose_name='responsable de la inactivacion de la clinica',
        on_delete=models.DO_NOTHING,
        null=True
    )

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.clinica, self.fecha_activacion, self.responsable_activacion, self.fecha_inactivacion, self.responsable_inactivacion)

    class Meta:
        db_table = 'sismeu\".\"historico_clinica'
        verbose_name = "Historico de la clinica"
        verbose_name = "Historicos de las clinicas"

#############################################################################
class MotivoInactivacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return'%s' % (self.nombre)

    class Meta:
        db_table = 'sismeu\".\"motivo_inactivacion'
        verbose_name = "Motivo de inactivacion"
        verbose_name_plural = "Motivos de inactivacion"
#############################################################################
class Region(models.Model):
    nombre = models.CharField(
        max_length=255,
        db_column='nombre',
        verbose_name="Nombre de la Región",
    )
    estado = models.ManyToManyField(
        'globales.Estado',
        verbose_name='Estado',
        related_name='estado_region',
        through='RegionEstado',
    )
    responsable = models.ManyToManyField(
        'cuenta.Persona',
        related_name='responsable',
        through='ResponsableRegional',
    )

    def __str__(self):
        return'%s' % (self.responsable)

    class Meta:
        db_table = 'sismeu\".\"region'
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
    
class ResponsableRegional(models.Model):
    region = models.ForeignKey(
        'Region',
        on_delete=models.CASCADE
    )
    responsable = models.ForeignKey(
        'cuenta.Persona',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return'%s' % (self.responsable)

    class Meta:
        db_table = 'sismeu\".\"responsable_region'

#############################################################################
class RegionEstado(models.Model):
    region = models.ForeignKey('Region', models.DO_NOTHING)
    estado = models.OneToOneField('globales.Estado',on_delete=models.PROTECT)

    def __str__(self):
        return'%s' % (self.estado)
    class Meta:
        db_table = 'sismeu\".\"region_estado'

#############################################################################

class AuditoriaClinica(models.Model):
    rif = models.CharField(
        max_length=30,
        db_column="rif_auditoria",
        verbose_name='rif de la clinica en auditoria',
    )
    nombre = models.CharField(
        max_length=255,
        db_column='nombre_auditoria',
        verbose_name='nombre de la clinica en auditoria'
    )
    estado = models.ForeignKey(
        'globales.Estado',
        verbose_name='estado de la clincia en auditoria',
        on_delete=models.PROTECT
    )
    municipio = models.ForeignKey(
        'globales.Municipio',
        verbose_name='municipio de la clinica en auditoria',
        on_delete=models.PROTECT
    )
    parroquia = models.ForeignKey(
        'globales.Parroquia',
        verbose_name='parroquia de la clinica en auditoria',
        on_delete=models.PROTECT,
        null = True,
        blank = True,
    )
    direccion = models.TextField()
    responsable = models.ForeignKey(
        'cuenta.Persona',
        verbose_name='Responsable de los cambios',
        on_delete=models.PROTECT
    )
    fecha = models.DateField(
        verbose_name='fecha de los cambios',
        auto_now_add=True,
    )

    def __str__ (self):
        return '%s, %s' % (self.rif, self.nombre)

    class Meta:
        db_table = 'sismeu\".\"auditoria_clinica'
        verbose_name = "Auditoria a la clinica"
        verbose_name_plural = "Auditorias a las clinicas"