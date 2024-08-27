from django.contrib import admin

from core.model.ocorrencia import Ocorrencia

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'descricao'
    ]