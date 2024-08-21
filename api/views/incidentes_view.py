from typing import List
from core.service import incidentes_service
from core.util.service_exception import ServiceException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def listar(request):
    try:
        paginacao = incidentes_service.buscar_por_filtro(request)
        
        return Response(paginacao)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )

@api_view(['GET'])
def buscar_por_id(request, id: int):

    try:
        incidente = incidentes_service.buscar_por_id(id)
        
        return Response(
            incidente
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['POST'])
def criar(request):

    try:
        incidente = incidentes_service.criar(
            request.data
        )

        return Response(
            incidente,
            status=status.HTTP_201_CREATED
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['PUT'])
def atualizar(request, id:int):

    try:
        incidente_atualizado = incidentes_service.atualizar(
            id,
            request.data
        )

        return Response(
            incidente_atualizado,
            status=status.HTTP_200_OK
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )

@api_view(['DELETE'])
def remover(request, id:int):

    try:
        incidentes_service.remover(id)

        return Response(
            {'mensagem': f'Incidente de id:{id} removido com sucesso!'},
            status=status.HTTP_204_NO_CONTENT
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )
    
@api_view(['DELETE'])
def remover_lista(request):

    try:
        ids: List[int] = request.data.get('ids', List[int])

        incidentes_service.remover_lista(ids)

        return Response(
            {'mensagem': f'Incidentes de id:{str(ids)} removidas com sucesso!'},
            status=status.HTTP_204_NO_CONTENT
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )