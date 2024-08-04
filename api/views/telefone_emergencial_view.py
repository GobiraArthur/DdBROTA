from typing import List
from core.service import telefone_emergencial_service
from core.util.service_exception import ServiceException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def criar(request):

    try:
        nova_categoria = telefone_emergencial_service.criar(
            request.data
        )

        return Response(
            nova_categoria,
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
        categoria_atualizada = telefone_emergencial_service.atualizar(
            id,
            request.data
        )

        return Response(
            categoria_atualizada,
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
        telefone_emergencial_service.remover(id)

        return Response(
            {'mensagem': f'Telefone emergencial de id:{id} removido com sucesso!'},
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

        telefone_emergencial_service.remover_lista(ids)

        return Response(
            {'mensagem': f'Telefones emergenciais de id:{str(ids)} removidas com sucesso!'},
            status=status.HTTP_204_NO_CONTENT
        )
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code
        )