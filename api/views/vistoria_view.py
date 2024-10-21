from typing import List
from core.service import vistoria_service
from core.util.service_exception import ServiceException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def listar(request):
    try:
        vistorias = vistoria_service.buscar_por_filtro(request)
        return Response(vistorias)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

@api_view(['GET'])
def buscar_por_id(request, id):
    try:
        vistoria = vistoria_service.buscar_por_id(id)

        return Response(vistoria)
    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

@api_view(['POST'])
def criar(request):
    try:
        nova_vistoria = vistoria_service.criar(request)

        return Response(nova_vistoria, status=status.HTTP_201_CREATED)

    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

@api_view(['PUT'])
def atualizar(request, id):
    try:
        vistoria_atualizada = vistoria_service.atualizar(id, request.data)

        return Response(vistoria_atualizada,
                        status=status.HTTP_200_OK)

    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

@api_view(['DELETE'])
def remover(request, id):
    try:
        vistoria_service.remover(id)

        return Response(
            {'mensagem': 'Vistoria deletada com sucesso'},
            status=status.HTTP_200_OK)

    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

@api_view(['DELETE'])
def remover_lista(request):
    try:
        ids: List[int] = request.data.get('ids', List[int])
        vistoria_service.remover_lista(ids)

        return Response(
            {'mensagem': 'Vistorias deletadas com sucesso'},
            status=status.HTTP_200_OK)

    except ServiceException as se:
        return Response(
            {'mensagem': se.msg},
            status=se.http_erro_code)

