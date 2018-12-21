# Librerias Django
from django.contrib import admin

# Librerias en carpetas locales
from .models import (
    Clinica, HistoricoClinica, MotivoInactivacion, Region,
    RegionEstado)

# Register your models here.

admin.site.register(Clinica)

# admin.site.register(ContactoClinica)
admin.site.register(HistoricoClinica)

admin.site.register(MotivoInactivacion)

admin.site.register(Region)

admin.site.register(RegionEstado)
# admin.site.register(TelefonoClinica)
