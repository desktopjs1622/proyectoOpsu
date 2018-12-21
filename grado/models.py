# Librerias Future
# Librerias Future
# Librerias Future
from __future__ import unicode_literals  # para los caracteres especiales

# Librerias Standard
from datetime import datetime  # para las fechas

# Librerias Django
from django.db import models
from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse_lazy


class Actogrado(models.Model):
    localidad = models.ForeignKey('oeu.Localidad', verbose_name='Localidad', on_delete=models.PROTECT)
    fecha_acto = models.DateField('Fecha',)
    num_acta = models.IntegerField()
    status = models.BooleanField(default = True)
    responsable = models.ForeignKey('cuenta.Persona', on_delete=models.PROTECT, db_column='responsable_id', verbose_name='Responsable')

    def __str__(self):
        return ' %s '% (self.num_acta )
    
    @property
    def num_acta_format(self):
        return str(self.num_acta).zfill(4)

    @property
    def get_absolute_url(self):
        return reverse_lazy('grado:act_detail', kwargs = {'pk':self.id})

    class Meta:
            db_table = 'grado\".\"actogrado'
            verbose_name = "Acto de Grado"
            verbose_name_plural = "Actos de Grado"



# @receiver(pre_save, sender=Actogrado)
# def actualizar_username(sender, instance, *args, **kwargs):
#     """Con esta función le asignamos el numero de acta correspondiente y la
#     localidad correspondiente al usuario"""
#     instance.num_acta = Actogrado.objects.filter(localidad_id=1193).latest('num_acta').num_acta + 1


################################################################################################################################################################################################################

class Graduando(models.Model):
    actogrado = models.ForeignKey('Actogrado', null=True, blank=True, on_delete=models.CASCADE, db_column='actogrado_id', verbose_name='Actos de Grado')
    persona = models.ForeignKey('globales.Saime', related_name='persona_id', null=True, blank=True, on_delete=models.PROTECT, db_column='persona_id', verbose_name='Persona')
    carrera = models.ForeignKey('oeu.carrera', related_name="carreraid", null=True, blank=True, on_delete=models.PROTECT, verbose_name='Carrera')
    libro = models.IntegerField(blank = True, null = True)
    folio = models.IntegerField(blank = True, null = True)
    num_asignado = models.IntegerField(verbose_name='Número de Asignado', null = True)
    responsable = models.ForeignKey('cuenta.Persona', related_name='func_responsable', null=True, blank=True, on_delete=models.PROTECT, db_column='responsable_func', verbose_name='Responsable')

    def __str__(self):
        return '%s' % (self.persona_id)

    class Meta:
            db_table = 'grado\".\"graduando'
            verbose_name = "Graduando"
            verbose_name_plural = "Graduandos"
            ordering = ['-num_asignado']



class LocalidadPersona(models.Model):
    persona = models.ForeignKey('cuenta.Persona', on_delete=models.PROTECT, verbose_name='Graduando')
    localidad = models.ForeignKey('oeu.localidad', on_delete=models.PROTECT, verbose_name='Localidad')

    def __str__(self):
        return '%s '% (self.localidad_id)

    class Meta:
            db_table = 'grado\".\"localidad_persona'
