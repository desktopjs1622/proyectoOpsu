# -*- coding: utf-8 -*-
"""
Modelo de la aplicación de Asuntos Laborales
"""
# Librerias Future
# Future Library
from __future__ import unicode_literals

# Librerias Standard
# Standard Library
from datetime import datetime

# Librerias Django
# Django Library
from django.db import models


###################################################################################################
class TipoSoporteFormal(models.Model):
    """
    """
    id_tipo_sf = models.AutoField(
        primary_key=True,
        db_column='id_tipo_soporte_formal'
    )
    nombre_tipo_sf = models.CharField(
        max_length=255,
        db_column='nombre_tipo_soporte_formal'
    )

    def __str__(self):
        return self.nombre_tipo_sf

    class Meta:
        db_table = 'asuntos_laborales\".\"tipo_sf'
        verbose_name = "Tipo SF"
        verbose_name_plural = "Tipos SF"


###################################################################################################
class SoporteFormal(models.Model):
    """
    """
    id_sf = models.AutoField(primary_key=True, db_column='id_soporte_formal')
    id_tipo_sf = models.ForeignKey(
        TipoSoporteFormal,
        models.DO_NOTHING,
        verbose_name='Tipo SF',
        db_column='id_tipo_soporte_formal',
        blank=True,
        null=True
    )
    descripcion_sf = models.CharField(
        max_length=255,
        db_column='descripcion_soporte_formal',
        verbose_name='Descripción SF'
    )
    fecha_sf = models.DateField(db_column='fecha_soporte_formal', verbose_name='Fecha SF')
    numero_sf = models.CharField(
        max_length=255,
        db_column='numero_soporte_formal',
        verbose_name='Número SF',
        blank=True,
        null=True
    )
    numero_gaceta = models.CharField(max_length=45, verbose_name='Gaceta SF', blank=True, null=True)
    fecha_gaceta = models.DateField(blank=True, verbose_name='Fecha Gaceta SF', null=True)
    creado = models.DateTimeField(blank=True, null=True)
    actualizado = models.DateTimeField(blank=True, null=True, default=datetime.now)
    # id_archivo = models.ManyToManyField(
    #     'globales.Archivo',
    #     db_column='id_soporte_formal',
    #     verbose_name="Anexos SF",
    #     db_table='asuntos_laborales\".\"archivo_sf',
    #     blank=True
    # )

    def __str__(self):
        return self.descripcion_sf

    class Meta:
        db_table = 'asuntos_laborales\".\"soporte_formal'
        verbose_name = "Soporte Formal"
        verbose_name_plural = "Soportes Formales"


###################################################################################################
class TipoPersonal(models.Model):
    """
    """
    nombre_tipo_personal = models.CharField(
        max_length=255,
        db_column='nombre_tipo_personal',
        verbose_name='Tipo Personal'
    )

    def __str__(self):
        return self.nombre_tipo_personal

    class Meta:
        db_table = 'asuntos_laborales\".\"tipo_personal'
        verbose_name = "Tipo de Personal"
        verbose_name_plural = "Tipos de Personal"


###################################################################################################
class Cargo(models.Model):
    """
    """
    nombre_cargo = models.CharField(
        max_length=255,
        db_column='nombre_cargo'
    )
    id_tipo_personal = models.ForeignKey(
        'TipoPersonal',
        models.DO_NOTHING,
        verbose_name='Tipo Personal',
        db_column='id_tipo_personal',
    )

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'asuntos_laborales\".\"cargo'
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


###################################################################################################
class Dedicacion(models.Model):
    """
    """
    nombre_dedicacion = models.CharField(
        max_length=255,
        db_column='nombre_dedicacion',
        verbose_name='Dedicación'
    )
    id_tipo_personal = models.ForeignKey(
        'TipoPersonal',
        models.DO_NOTHING,
        verbose_name='Tipo Personal',
        db_column='id_tipo_personal'
    )
    id_cargo = models.ForeignKey(
        'Cargo',
        models.DO_NOTHING,
        verbose_name='Cargo',
        db_column='id_cargo'
    )
    
    def __str__(self):
        return self.nombre_dedicacion

    class Meta:
        db_table = 'asuntos_laborales\".\"dedicacion'
        verbose_name = "Dedicación"
        verbose_name_plural = "Dedicaciones"


###################################################################################################
class SueldoBasico(models.Model):
    """
    """
    id_tipo_institucion = models.ForeignKey(
        'oeu.TipoInstitucion',
        models.DO_NOTHING,
        db_column='id_tipo_institucion',
        verbose_name="Tipo IEU",
        blank=True,
        null=True,
        related_name='tipoInstitucion3'
    )
    id_tipo_institucion_especifico = models.ForeignKey(
        'oeu.SubTipoInstitucion',
        models.DO_NOTHING,
        verbose_name='Sub Tipo Institucion',
        db_column='id_tipo_institucion_especifico'
    )
    id_tipo_institucion_detalle = models.ForeignKey(
        'oeu.TipoInstitucionDetalle',
        models.DO_NOTHING,
        verbose_name='Tipo IEU Detalle',
        db_column='id_tipo_institucion_detalle'
    )
    id_institucion = models.ForeignKey(
        'oeu.Institucion',
        models.DO_NOTHING,
        verbose_name='Institución',
        db_column='id_institucion'
    )
    id_tipo_personal = models.ForeignKey(
        'TipoPersonal',
        models.DO_NOTHING,
        verbose_name='Tipo Personal',
        db_column='id_tipo_personal'
    )
    cargo = models.ForeignKey(
        'Cargo',
        models.DO_NOTHING,
        verbose_name='Cargo',
        db_column='id_cargo'
    )
    dedicacion = models.ForeignKey(
        'Dedicacion',
        models.DO_NOTHING,
        verbose_name='Dedicación',
        db_column='id_dedicacion'
    )
    desde = models.DateField(
        db_column='desde',
        verbose_name='Desde'
    )
    hasta = models.DateField(
        db_column='hasta',
        verbose_name='Hasta'
    )
    sueldo = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Sueldo',
        db_column='sueldo'
    )
    sf = models.ManyToManyField(
        'SoporteFormal',
        db_column='id_soporte_formal',
        verbose_name="Soporte Formal",
        db_table='asuntos_laborales\".\"sueldo_sf',
        blank=True
    )

    class Meta:
        db_table = 'asuntos_laborales\".\"sueldo_basico'
        verbose_name = "Sueldo Básico"
        verbose_name_plural = "Sueldos Básicos"


###################################################################################################
class Prima(models.Model):
    """
    """
    nombre_prima = models.CharField(
        max_length=255,
        db_column='nombre_prima',
        verbose_name='Prima'
    )
    id_tipo_institucion = models.ForeignKey(
        'oeu.TipoInstitucion',
        models.DO_NOTHING,
        db_column='id_tipo_institucion',
        verbose_name="Tipo IEU",
        blank=True,
        null=True,
        related_name='tipoInstitucion4'
    )
    id_tipo_institucion_especifico = models.ForeignKey(
        'oeu.SubTipoInstitucion',
        models.DO_NOTHING,
        verbose_name='Sub Tipo Institucion',
        db_column='id_tipo_institucion_especifico'
    )
    id_tipo_institucion_detalle = models.ForeignKey(
        'oeu.TipoInstitucionDetalle',
        models.DO_NOTHING,
        verbose_name='Tipo IEU Detalle',
        db_column='id_tipo_institucion_detalle'
    )
    id_institucion = models.ForeignKey(
        'oeu.Institucion',
        models.DO_NOTHING,
        verbose_name='Institución',
        db_column='id_institucion'
    )
    id_tipo_personal = models.ForeignKey(
        'TipoPersonal',
        models.DO_NOTHING,
        verbose_name='Tipo Personal',
        db_column='id_tipo_personal'
    )
    cargo = models.ForeignKey(
        'Cargo',
        models.DO_NOTHING,
        verbose_name='Cargo',
        db_column='id_cargo'
    )
    dedicacion = models.ForeignKey(
        'Dedicacion',
        models.DO_NOTHING,
        verbose_name='Dedicación',
        db_column='id_dedicacion'
    )
    desde = models.DateField(
        db_column='desde',
        verbose_name='Desde'
    )
    hasta = models.DateField(
        db_column='hasta',
        verbose_name='Hasta'
    )
    monto_prima = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Monto Prima',
        db_column='monto_prima'
    )
    # sf = models.ManyToManyField(
    #     'SoporteFormal',
    #     db_column='id_soporte_formal',
    #     verbose_name="Soporte Formal",
    #     db_table='asuntos_laborales\".\"prima_sf',
    #     blank=True
    # )

    class Meta:
        db_table = 'asuntos_laborales\".\"prima'
        verbose_name = "Prima"
        verbose_name_plural = "Primas"


###############################################################################
class Categoria(models.Model):
    """
    """
    nombre = models.CharField(max_length=255)

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"categoria'

    def __str__(self):
        return self.nombre


class CondicionEgreso(models.Model):
    """
    """
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"condicion_egreso'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class HistoriaLaboral(models.Model):
    """
    """
    persona = models.ForeignKey('globales.Saime', models.DO_NOTHING)
    institucion = models.ForeignKey('oeu.Institucion', models.DO_NOTHING)
    tipo_personal = models.ForeignKey('TipoPersonal', models.DO_NOTHING)
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()
    condicion_egreso = models.ForeignKey(CondicionEgreso, models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.persona, self.institucion)

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"historia_laboral'
        verbose_name = 'Historia Laboral'
        verbose_name_plural = 'Historias Laborales'


class HlDesembolso(models.Model):
    """
    """
    historia_laboral = models.ForeignKey(HistoriaLaboral, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo_desembolso = models.ForeignKey('TipoDesembolso', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.historia_laboral

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"hl_desembolso'
        verbose_name = 'Desembolso de Prestaciones Sociales de la Historia Laboral'
        verbose_name_plural = 'Desembolsos de Prestaciones Sociales de la Historia Laboral'
        ordering = ['fecha',]


class HlCategoria(models.Model):
    """
    """
    historia_laboral = models.ForeignKey(HistoriaLaboral, models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    grado = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.historia_laboral, self.categoria)

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"hl_categoria'
        verbose_name = 'Categoria de la Historia Laboral'
        verbose_name_plural = 'Categorias de la Historia Laboral'


class HlDedicacion(models.Model):
    """
    """
    historia_laboral = models.ForeignKey(HistoriaLaboral, models.DO_NOTHING, blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    dedicacion = models.ForeignKey(Dedicacion, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.historia_laboral, self.dedicacion)

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"hl_dedicacion'
        verbose_name = 'Dedicación de la Historia Laboral'
        verbose_name_plural = 'Dedicaciones de la Historia Laboral'


class HlPermiso(models.Model):
    """
    """
    historia_laboral = models.ForeignKey(HistoriaLaboral, models.DO_NOTHING, blank=True, null=True)
    tipo_permiso = models.ForeignKey('TipoPermiso', models.DO_NOTHING, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    descuenta = models.NullBooleanField(default=False)

    def __str__(self):
        return self.historia_laboral

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"hl_permiso'
        verbose_name = 'Permiso de la Historia Laboral'
        verbose_name_plural = 'Permisos de la Historia Laboral'


class HlSalarioIntegralAnual(models.Model):
    """
    """
    historia_laboral = models.ForeignKey(HistoriaLaboral, models.DO_NOTHING, blank=True, null=True)
    fecha_desde = models.DateField(blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)
    sueldo = models.FloatField(blank=True, null=True)
    antiguedad = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.historia_laboral)

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"hl_salario_integral_anual'
        verbose_name = 'Salario Integral Anual de la Historia Laboral'
        verbose_name_plural = 'Salarios Integrales Anuales de la Historia Laboral'


class TasaInteres(models.Model):
    """
    """
    fecha_desde = models.DateTimeField(blank=True, null=True)
    fecha_hasta = models.DateTimeField(blank=True, null=True)
    tasa_pasiva = models.FloatField(blank=True, null=True)
    tasa_promedio = models.FloatField(blank=True, null=True)
    tasa_activa = models.FloatField(blank=True, null=True)
    tasa_90_dias = models.FloatField(blank=True, null=True)
    interest_rate = models.FloatField(blank=True, null=True)
    stage_type = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"tasa_interes'


class TipoCategoria(models.Model):
    """
    """
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    iniciales = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"tipo_categoria'


class TipoDesembolso(models.Model):
    """
    """
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"tipo_desembolso'


class TipoPermiso(models.Model):
    """
    """
    nombre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        """
        """
        db_table = 'asuntos_laborales\".\"tipo_permiso'
