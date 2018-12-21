from django.db import models
from cuenta.models import Persona
from globales.models import Estado
# Create your models here.

class SeguidorEstadal(models.Model):
    persona = models.ForeignKey(
        'cuenta.Persona',
        verbose_name="Seguidor de estados",
        on_delete=models.DO_NOTHING
    )
    estado = models.ManyToManyField(
        'globales.Estado',
        verbose_name="Estados a dar seguimiento",
        related_name="estado_seguidor"
    )

    def __str__(self):
        return '%s %s' % (
            self.persona, self.estado
        )
    class Meta:
        db_table = 'pni\".\"seguidor_estadal'
        verbose_name = "Seguidor Estadal"
        verbose_name_plural = "Seguidores Estadales"