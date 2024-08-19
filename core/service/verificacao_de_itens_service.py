from typing import List
from django.http import HttpRequest
from core.util.generic_paginator import GenericPaginator
from core.util.service_exception import ServiceException
from rest_framework import status
from api.serializers.verificacao_de_itens_serializer import VerificacaoDeItensAtualizacaoSerializer
from api.serializers.verificacao_de_itens_serializer import VerificacaoDeItensCadastroSerializer
from api.serializers.verificacao_de_itens_serializer import VerificacaoDeItensSerializer
from core.model.verificacao_de_itens import VerificacaoDeItens

def buscar_por_filtro(request: HttpRequest) -> List[VerificacaoDeItens]:
    g_paginator = GenericPaginator(
        VerificacaoDeItens,
        VerificacaoDeItensSerializer
    )

    ordenacao = request.GET.get('ordenacao', None)
    filtro_nome = request.GET.get('nome', None)
    pag = request.GET.get('pag', None)
    max_reg_pag = request.GET.get('max_reg_pag', None)

    g_paginator.set_pag(pag)
    g_paginator.set_max_reg_pag(max_reg_pag)
    g_paginator.set_ordenacao(ordenacao)

    if filtro_nome:
        g_paginator.queryset = g_paginator.queryset.filter(nome__icontains=filtro_nome)

    return g_paginator.get_objeto_para_view()

def buscar_por_id(id: int) -> VerificacaoDeItens:
    try:
        verificacao_de_itens = VerificacaoDeItens.objects.get(pk=id)
        serializer = VerificacaoDeItensSerializer(verificacao_de_itens)

        return serializer.data
    except VerificacaoDeItens.DoesNotExist:
        raise ServiceException(
            f'Item de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND)
    
def criar(data):
    serializer = VerificacaoDeItensCadastroSerializer(data=data)

    if serializer.is_valid():
        if VerificacaoDeItens.objects.filter(nome=serializer.validated_data.get('nome')).exists():
            raise ServiceException(
                f'Item de verificação já cadastrado!',
                status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return serializer.data
    else:
        raise ServiceException(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
def atualizar(id: int, data):
    try:
        verificacao_de_itens = VerificacaoDeItens.objects.get(pk=id)
        serializer = VerificacaoDeItensAtualizacaoSerializer(verificacao_de_itens, data=data, partial=True)
        if serializer.is_valid():
            if VerificacaoDeItens.objects.exclude(pk=id).filter(nome=serializer.validated_data.get('nome')).exists():
                raise ServiceException(
                    f'Item de verificação já cadastrado!',
                    status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return serializer.data
        else:
            raise ServiceException(serializer.errors, status.HTTP_400_BAD_REQUEST)
    except VerificacaoDeItens.DoesNotExist:
        raise ServiceException(
            f'Item de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND)
    
def remover(id: int):
    try:
        verificacao_de_itens = VerificacaoDeItens.objects.get(pk=id)
        verificacao_de_itens.delete()
    except VerificacaoDeItens.DoesNotExist:
        raise ServiceException(
            f'Item de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )
    
def remover_lista(ids: List[int]):
    if not ids:
        raise ServiceException(
            'A lista precisa conter ao menos um elemento',
            status.HTTP_400_BAD_REQUEST)
    verificacao_de_itens = VerificacaoDeItens.objects.filter(id__in=ids)
    if verificacao_de_itens.exists():
        verificacao_de_itens.delete()
