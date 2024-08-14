from django.http import HttpRequest
from requests import Response
from core.model.necessidades_de_manutencao import NecessidadeDeManutencao
from rest_framework import status
from typing import List
from core.util.service_exception import ServiceException
from core.util.generic_paginator import GenericPaginator
from api.serializers.necessidades_de_manutencao_serializer import NecessidadesDeManutencaoSerializer, NecessidadesDeManutencaoCadastroSerializer, NecessidadesDeManutencaoAtualizacaoSerializer

def criar(data):
    serializer = NecessidadesDeManutencaoCadastroSerializer(data=data)
    if serializer.is_valid(): 
        if NecessidadeDeManutencao.objects.filter(nome=serializer.validated_data.get('nome')).exists():
            raise ServiceException(
                f'Item de manutenção já cadastrada!',
                status.HTTP_400_BAD_REQUEST)       
        serializer.save()          #precisa de mais alguma validacao? Manutenção ja cadastrada ok
        return serializer.data
    else:
        raise ServiceException(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST)
    

def atualizar(id: int, data):
    try:
        necessidade = NecessidadeDeManutencao.objects.get(pk=id)
        serializer = NecessidadesDeManutencaoAtualizacaoSerializer(necessidade, data=data, partial=True)
        if serializer.is_valid():
            if NecessidadeDeManutencao.objects.exclude(pk=id).filter(nome=serializer.validated_data.get('nome')
            ).exists():
                raise ServiceException(
                    f'Item de manutenção já cadastrada!',
                    status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return serializer.data
        else:
            raise ServiceException(serializer.errors, status.HTTP_400_BAD_REQUEST)
    except NecessidadeDeManutencao.DoesNotExist:
        raise ServiceException(
            f'Item de manutenção de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND)
    
def remover(id: int):
    try:
        necessidade = NecessidadeDeManutencao.objects.get(pk=id)
        necessidade.delete()
    except NecessidadeDeManutencao.DoesNotExist:
        raise ServiceException(
            f'Item de manutenção de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )
    
def buscar_por_id(id: int):
    try:
        necessidade = NecessidadeDeManutencao.objects.get(pk=id)
        return NecessidadesDeManutencaoSerializer(necessidade).data
    except NecessidadeDeManutencao.DoesNotExist:
        raise ServiceException(
            f'Item de manutenção de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )
    
def buscar_por_filtro(request: HttpRequest) -> List[NecessidadeDeManutencao]:
    g_paginator = GenericPaginator(NecessidadeDeManutencao, NecessidadesDeManutencaoSerializer)
    ordenacao = request.GET.get('ordenacao', None)

    filtro_nome = request.GET.get('nome', None)
    
    pag = request.GET.get('pag', None)
    max_reg_pag = request.GET.get('max_reg_pag', None)

    g_paginator.set_pag(pag)
    g_paginator.set_max_reg_pag(max_reg_pag)
    g_paginator.set_ordenacao(ordenacao)
    
    if filtro_nome:
        g_paginator.queryset = g_paginator.queryset.filter(numero__startswith=filtro_nome)

    return g_paginator.get_objeto_para_view()

    