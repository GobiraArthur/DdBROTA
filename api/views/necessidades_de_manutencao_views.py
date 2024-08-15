from typing import List
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.service import necessidade_de_manutencao_service
from core.util.service_exception import ServiceException

@api_view(['GET'])
def listar(request):
    try:
        itens = necessidade_de_manutencao_service.buscar_por_filtro(request)
        
        return Response(itens)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['GET'])
def buscar_por_id(request, id: int):

    try:
        item = necessidade_de_manutencao_service.buscar_por_id(id)
        
        return Response(item)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['POST'])
def criar(request):

    try:
        novo_item_de_manutencao = necessidade_de_manutencao_service.criar(request.data)

        return Response(novo_item_de_manutencao, status=status.HTTP_201_CREATED)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['PUT'])
def atualizar(request, id:int):

    try:
        item_atualizado = necessidade_de_manutencao_service.atualizar(id, request.data)

        return Response(item_atualizado)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['DELETE'])
def deletar(request, id:int):

    try:
        necessidade_de_manutencao_service.remover(id)

        return Response(status=status.HTTP_204_NO_CONTENT)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

@api_view(['DELETE'])
def deletar_lista(request):
    try:
        ids: List[int] = request.data.get('ids', List[int])

        necessidade_de_manutencao_service.remover_lista(ids)

        return Response(
            {'mensagem': f'Itens de manutenção de id:{str(ids)} removidos com sucesso!'},
            status=status.HTTP_204_NO_CONTENT
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )