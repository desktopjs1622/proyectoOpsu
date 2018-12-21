""" Manejo de Fechas """
# Librerias Django
from django.db.models import Avg, Count, Max, Min, Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone

""" Manejo de funciones en BD """


def date(condicion):
    if condicion == 'year':
        return timezone.now().year
    elif condicion == 'last_year':
         return (timezone.now().year - 1)
    elif condicion == 'days':
         return timezone.now().days
    elif condicion == 'month':
        return timezone.now().month
    elif condicion == 'formateada':
        return timezone.now().strftime('%d de %B de %Y')
    elif condicion == 'now':
        return timezone.now()

def qs(modelo,**kwargs):
    if kwargs == None:
        return modelo.objects.all().order_by('-id')
    else:
        return modelo.objects.filter(**kwargs).order_by('-id')

def qs404(modelo,**kwargs):
    get_object_or_404(modelo, **kwargs)
