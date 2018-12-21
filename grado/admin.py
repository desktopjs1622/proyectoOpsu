# Librerias Django
from django.contrib import admin

# Librerias en carpetas locales
from .forms import ActogradoForm, GraduandoForm, LocalidadPersonaForm
from .models import Actogrado, Graduando, LocalidadPersona


class GraduandoInline(admin.TabularInline):
    model = Graduando
    extra = 1

@admin.register(Graduando)
class GraduandoAdmin(admin.ModelAdmin):
    
    fields = [
        # 'cod_institucion',
        # 'localidad',
        'carrera',
        'persona',
        'actogrado',
        'responsable',
        'libro',
        'folio',
        'num_asignado'
    ]
    form = GraduandoForm
    search_fields = ['actogrado','libro','folio','num_asignado',]
    list_display = ['actogrado_id','num_asignado','libro','folio',]
    ordering = ['num_asignado',]
    show_full_result_count = True
    actions_selection_counter = True


##########################################################################################################
@admin.register(Actogrado)
class ActoGradoAdmin(admin.ModelAdmin):
    
    fields = [
        'localidad',
        'fecha_acto',
        'num_acta',
        'status',
        'responsable',
    ]

    form = ActogradoForm
    search_fields = ['localidad','fecha_acto','num_acta',]
    list_display = ['localidad','fecha_acto','num_acta',]
    ordering = ['fecha_acto',]
    show_full_result_count = True
    actions_selection_counter = True
#     inlines = [GraduandoInline,]


############################################################################################


@admin.register(LocalidadPersona)
class LocalidadPersonaAdmin(admin.ModelAdmin):
    
    fields = [
        'persona',
        'localidad',
        
    ]

    form = LocalidadPersonaForm
    search_fields = ['persona',]
    list_display = ['localidad_id','persona',]
    ordering = ['persona',]
    show_full_result_count = True
    actions_selection_counter = True
    #inlines = [GraduandoInline,]
