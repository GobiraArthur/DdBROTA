from django.contrib import admin
from core.model.necessidades_de_manutencao import NecessidadeDeManutencao

@admin.register(NecessidadeDeManutencao)
class NecessidadeDeManutencaoAdmin(admin.ModelAdmin):    #personalizando interface administrativa
    list_display = ('id', 'nome')   
        
    