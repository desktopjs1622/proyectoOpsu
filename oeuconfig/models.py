"""
Modelo de datos de la app OEU
"""
# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.db import models


##############################################################################
class RequisitoIngreso(models.Model):
    """Modelo para gestionar los requisitos de ingresos a las localidades de
    las localidades de las IEU.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"requisito_ingreso'
        verbose_name = "Requisito de Ingreso"
        verbose_name_plural = "Requisitos de Ingreso"


##############################################################################
class Servicio(models.Model):
    """
    Modelo para agregar/editar/eliminar/visualizar los servicios que se ofrecen en las IEU
    y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"servicio'
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"


##############################################################################
class DependenciaAdministrativa(models.Model):
    """
    Modelo para agregar/editar/eliminar/visualizar las dependencias
    administrativas que se encuentran en las IEU y clase que pertenece al
    modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"dependencia_administrativa'
        verbose_name = "Dependencia Administrativa"
        verbose_name_plural = "Dependencias Administrativas"


##############################################################################
class TipoSoporteFormalCambio(models.Model):
    """Modelo para la gestión de los Tipos de Soportes Formales de Cambios
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"tipo_sfc'
        verbose_name = "Tipo SFC"
        verbose_name_plural = "Tipos SFC"


##############################################################################
class SoporteFormalCambio(models.Model):
    """Modelo para la gestión de los Soportes Formales de Cambios
    """

    tipo_sfc = models.ForeignKey(
        TipoSoporteFormalCambio, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    numero_gaceta = models.CharField(max_length=45, blank=True, null=True)
    fecha_gaceta = models.DateField(blank=True, null=True)
    archivo_adjunto = models.FileField(
        upload_to="archivo_adjunto_sfc/",
        null=True,
        blank=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.creado = datetime.now
    #     self.actualizado = datetime.now

    #     return super(SoporteFormalCambio, self).save(*args, **kwargs)

    class Meta:
        db_table = 'oeu\".\"soporte_formal_cambio'
        verbose_name = "Soporte Formal de Cambio"
        verbose_name_plural = "Soportes Formales de Cambio"


##############################################################################
class Activacion(models.Model):
    """agregar comentario de la clase
    """
    cod_activacion = models.CharField(primary_key=True, max_length=8)
    interpretacion = models.CharField(max_length=255)

    def __str__(self):
        return self.cod_activacion

    class Meta:
        db_table = 'oeu\".\"activacion'


##############################################################################
class Bitacora(models.Model):
    """agregar comentario de la clase
    """
    id_bitacora = models.AutoField(primary_key=True)
    nombre_tabla = models.CharField(max_length=64)
    datos_registro = models.TextField()  # This field type is a guess.
    fecha_hora_registro = models.DateTimeField()

    class Meta:
        db_table = 'oeu\".\"bitacora'


##############################################################################
class InstanciaAdministrativa(models.Model):
    """
    Este modelo controla las instancias administrativas para luego poder
    referenciar los teléfonos, correos, etc. de las localidades de las IEU
    """
    nombre = models.CharField(max_length=100)
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre', ]
        db_table = 'oeu\".\"instancia_administrativa'
        verbose_name = "Instancia Administrativa"
        verbose_name_plural = "Instancias Administrativas"


##############################################################################
class Modalidad(models.Model):
    """Modalidades de estudios en las IEU y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre', ]
        db_table = 'oeu\".\"modalidad'
        verbose_name = "Régimen de Estudio"
        verbose_name_plural = "Regímenes de Estudio"


##############################################################################
class AyudaEconomica(models.Model):
    """ modelo de los tipos de ayuda economicas y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        db_table = 'oeu\".\"tipo_ayuda_economica'
        verbose_name = "Ayuda Económica"
        verbose_name_plural = "Ayudas Económicas"


##############################################################################
class TipoCarrera(models.Model):
    """Modelo para gestionar los tipos de carrera que se dictan en las IEU
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"tipo_carrera'
        verbose_name = "Tipo de Programa Académico"
        verbose_name_plural = "Tipos de Programa Académico"


##############################################################################
class TipoLocalidad(models.Model):
    """Modelo para gestionar los tipos de localidad de las IEU.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"tipo_localidad'
        verbose_name = "Tipo de localidad"
        verbose_name_plural = "Tipos de localidad"


##############################################################################
class Titulo(models.Model):
    """ Modelo para gestionar los titulos que se otorgan en las IEU.
    """
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre', ]
        db_table = 'oeu\".\"titulo'
        verbose_name = "Título"
        verbose_name_plural = "Títulos"


##############################################################################
class TipoTurnoDeEstudio(models.Model):
    """Modelo para agregar/editar/eliminar/visualizar los turnos que se otorgan en las IEU
        y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"turno'
        verbose_name = "Turno de Estudio"
        verbose_name_plural = "Turnos de Estudio"


##############################################################################
class ActividadCultural(models.Model):
    """Modelo para agregar/editar/eliminar/visualizar las actividades culturales que se otorgan en las IEU
        y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"actividad_cultural'
        verbose_name = "Actividad Cultural"
        verbose_name_plural = "Actividades Culturales"


##############################################################################
class DisciplinaDeportiva(models.Model):
    """ Modelo para agregar/editar/eliminar/visualizar las disciplinas deportivas que se otorgan en las IEU
        y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"disciplina_deportiva'
        verbose_name = "Disciplina Deportiva"
        verbose_name_plural = "Disciplinas Deportivas"


##############################################################################
class OrganizacionEstudiantil(models.Model):
    """ Modelo para agregar/editar/eliminar/visualizar las organizaciones estudiantiles que se otorgan en las IEU
    y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"organizacion_estudiantil'
        verbose_name = "Organizacion Estudiantil"
        verbose_name_plural = "Organizaciones Estudiantiles"


##############################################################################
class AgrupacionCivica(models.Model):
    """ Modelo para agregar/editar/eliminar/visualizar las agrupaciones cívicas que se otorgan en las IEU
        y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"agrupacion_civica'
        verbose_name = "Agrupación Civica"
        verbose_name_plural = "Agrupaciones Civicas"


##############################################################################
class RedSocial(models.Model):
    """ Modelo para agregar/editar/eliminar/visualizar las redes sociales que se otorgan en las IEU
        y clase que pertenece al modulo modelo_simple_listar.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'oeu\".\"red_social'
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
