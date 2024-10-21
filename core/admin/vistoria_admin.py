from django.contrib import admin
from core.model.vistoria import Vistoria, VistoriaIncidente, VistoriaNecessidadeManutencao, VistoriaVerificacaoItens

class VistoriaIncidenteInline(admin.TabularInline):
    model = VistoriaIncidente
    extra = 1

class VistoriaNecessidadeManutencaoInline(admin.TabularInline):
    model = VistoriaNecessidadeManutencao
    extra = 1

class VistoriaVerificacaoItensInline(admin.TabularInline):
    model = VistoriaVerificacaoItens
    extra = 1

@admin.register(Vistoria)
class VistoriaAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'data',
        'entrada',
        'saida',
        'motorista',
        'veiculo',
        'criado_em',
        'atualizado_em',
        'deletado_em'
    ]
    inlines = [
        VistoriaIncidenteInline,
        VistoriaNecessidadeManutencaoInline,
        VistoriaVerificacaoItensInline
    ]
    
