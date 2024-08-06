from rest_framework.serializers import ModelSerializer
from django.db.models import Model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class GenericPaginator():

    def __init__(self, object_class: Model, serializer_class: ModelSerializer) -> None:
        self.pag = 1
        self.max_reg_pag = 10
        self.serializer_class: ModelSerializer = serializer_class
        self.queryset = object_class.objects.all()
        self.ordenacao = None

    def set_ordenacao(self, ordenacao):
        self.ordenacao = ordenacao
        if ordenacao:
            self.queryset = self.queryset.order_by(ordenacao)
        else:
            self.queryset = self.queryset.order_by('id')

    def set_pag(self, pag):
        if pag:
            self.pag = int(pag)

    def set_max_reg_pag(self, max_reg_pag):
        if max_reg_pag:
            self.max_reg_pag = int(max_reg_pag)
        

    def get_registro_por_pagina(self):
        try:
            p_registros = self.p.page(self.pag)
        except PageNotAnInteger:
            p_registros = self.p.page(1)
        except EmptyPage:
            p_registros = self.p.page(self.p.num_pages)
        
        return p_registros
    
    def get_objeto_para_view(self):

        self.p = Paginator(
            self.queryset,
            self.max_reg_pag
        )
        
        try:
            p_registros = self.p.page(self.pag)
        except PageNotAnInteger:
            p_registros = self.p.page(1)
        except EmptyPage:
            p_registros = self.p.page(self.p.num_pages)

        serializer = self.serializer_class(p_registros, many=True)

        return {
            'registros': serializer.data,
            'total_registros': self.p.count,
            'max_registros_pagina': self.max_reg_pag,
            'pagina_atual': self.pag,
            'total_paginas': self.p.num_pages,
            'proxima': p_registros.next_page_number() if p_registros.has_next() else None,
            'anterior': p_registros.previous_page_number() if p_registros.has_previous() else None,
            'ordenacao': self.ordenacao
        }