from typing import List

from django.http import HttpRequest
from api.serializers.incidentes_serializer import IncidentesAtualizacaoSerializer, IncidentesCadastroSerializer, IncidentesSerializer
from core.model.incidentes import Incidentes
from core.util.generic_paginator import GenericPaginator
from core.util.service_exception import ServiceException
from rest_framework import status


def buscar_por_filtro(request: HttpRequest) -> List[Incidentes]:

    g_paginator = GenericPaginator(
        Incidentes,
        IncidentesSerializer
    )

    ordenacao = request.GET.get('ordenacao', None)

    
    pag = request.GET.get('pag', None)
    max_reg_pag = request.GET.get('max_reg_pag', None)

    g_paginator.set_pag(pag)
    g_paginator.set_max_reg_pag(max_reg_pag)
    g_paginator.set_ordenacao(ordenacao)
    

    return g_paginator.get_objeto_para_view()

def buscar_por_id(id: int) -> Incidentes:
    try:
        incidente = Incidentes.objects.get(pk=id)
        serializer = IncidentesSerializer(incidente)

        return serializer.data
    except Incidentes.DoesNotExist:
        raise ServiceException(
            f'Incidente de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )

def criar(data):

    serializer = IncidentesCadastroSerializer(
        data=data
    )

    if serializer.is_valid():
        objeto_criado = serializer.save()

        return IncidentesSerializer(objeto_criado).data
    else:
        raise ServiceException(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

def atualizar(id:int,data):

    try:
        incidente = Incidentes.objects.get(pk=id)
    except Incidentes.DoesNotExist:
        raise ServiceException(
            f'Incidente de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )
    
    serializer = IncidentesAtualizacaoSerializer(
        incidente,
        data=data,
        partial=True
    )

    if serializer.is_valid():
        objeto_criado = serializer.save()

        return IncidentesSerializer(objeto_criado).data
    else :
        raise ServiceException(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

def remover(id:int):

    try:
        incidente = Incidentes.objects.get(pk=id)
        
        incidente.delete()
    except Incidentes.DoesNotExist:
        raise ServiceException(
            f'Incidente de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )

def remover_lista(ids: List[int]):
    if not ids:
        raise ServiceException(
            f'A lista precisa conter ao menos um elemento',
            status.HTTP_400_BAD_REQUEST
        )
    
    incidente = Incidentes.objects.filter(id__in=ids) 

    if incidente.exists():
        incidente.delete()