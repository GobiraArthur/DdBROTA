from typing import List 
from core.service import verificacao_de_itens_service
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.util.service_exception import ServiceException

@api_view(['GET'])
def listar(request):
    try:
        paginacao = verificacao_de_itens_service.buscar_por_filtro(request)
        return Response(paginacao)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)
    
@api_view(['GET'])
def buscar_por_id(request, id: int):
    try:
        verificacao_de_itens = verificacao_de_itens_service.buscar_por_id(id)
        return Response(verificacao_de_itens)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)
    
@api_view(['POST'])
def criar(request):
    try:
        novo_item = verificacao_de_itens_service.criar(request.data)
        return Response(novo_item, status=status.HTTP_201_CREATED)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)
    
@api_view(['PUT'])
def atualizar(request, id:int):
    try:
        item_atualizado = verificacao_de_itens_service.atualizar(id, request.data)
        return Response(item_atualizado)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)
    
@api_view(['DELETE'])
def remover(request, id:int):
    try:
        verificacao_de_itens_service.remover(id)
        return Response(
            {'mensagem': f'Item de id:{id} removido com sucesso!'},
            status=status.HTTP_204_NO_CONTENT
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)
    
@api_view(['DELETE'])
def remover_lista(request):
    try:
        ids: List[int] = request.data.get('ids', List[int])
        verificacao_de_itens_service.remover_lista(ids)
        return Response(
            {'mensagem': 'Itens removidos com sucesso!'},
            status=status.HTTP_204_NO_CONTENT)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)