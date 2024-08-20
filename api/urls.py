from django.urls import path
from api.views import telefone_emergencial_view
from api.views import incidentes_view
from api.views import necessidades_de_manutencao_views

urlpatterns = [
    # Telefone Emergencial
    path('telefone/', telefone_emergencial_view.listar),
    path('telefone/<int:id>/', telefone_emergencial_view.buscar_por_id),
    path('telefone/criar/', telefone_emergencial_view.criar),
    path('telefone/atualizar/<int:id>/', telefone_emergencial_view.atualizar),
    path('telefone/remover/<int:id>/', telefone_emergencial_view.remover),
    path('telefone/remover/', telefone_emergencial_view.remover_lista),
    # Incidentes
    path('incidentes/', incidentes_view.listar),
    path('incidentes/<int:id>/', incidentes_view.buscar_por_id),
    path('incidentes/criar/', incidentes_view.criar),
    path('incidentes/atualizar/<int:id>/', incidentes_view.atualizar),
    path('incidentes/remover/<int:id>/', incidentes_view.remover),
    path('incidentes/remover/', incidentes_view.remover_lista),
    # Necessidade de Manutenção 
    path('necessidade/', necessidades_de_manutencao_views.listar),
    path('necessidade/<int:id>/', necessidades_de_manutencao_views.buscar_por_id),
    path('necessidade/criar/', necessidades_de_manutencao_views.criar),
    path('necessidade/atualizar/<int:id>/', necessidades_de_manutencao_views.atualizar),
    path('necessidade/remover/<int:id>/', necessidades_de_manutencao_views.deletar), 
    path('necessidade/remover/', necessidades_de_manutencao_views.deletar_lista)
]
