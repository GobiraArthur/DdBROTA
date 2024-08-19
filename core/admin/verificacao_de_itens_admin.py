from django.contrib import admin
from core.model.verificacao_de_itens import VerificacaoDeItens

@admin.register(VerificacaoDeItens)
class VerificacaoDeItensAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'nome',
        'criado_em'
    ]