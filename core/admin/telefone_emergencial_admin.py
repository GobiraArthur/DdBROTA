from django.contrib import admin

from core.model.telefone_emergencial import TelefoneEmergencial

@admin.register(TelefoneEmergencial)
class TelefoneEmergencialAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'numero',
        'criado_em'
    ]