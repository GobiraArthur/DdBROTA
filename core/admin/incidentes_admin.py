from django.contrib import admin

from core.model.incidentes import Incidentes

@admin.register(Incidentes)
class IncidentesAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'tipo',
        'descricao'
    ]