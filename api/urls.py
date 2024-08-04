from django.urls import path

from api.views import telefone_emergencial_view

urlpatterns = [
    # Telefone Emergencial
    path('telefone/criar/', telefone_emergencial_view.criar),
    path('telefone/atualizar/<int:id>/', telefone_emergencial_view.atualizar),
    path('telefone/remover/<int:id>/', telefone_emergencial_view.remover),
    path('telefone/remover/', telefone_emergencial_view.remover_lista),
]
