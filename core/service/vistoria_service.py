from typing import List
from django.http import HttpRequest
from core.util.generic_paginator import GenericPaginator
from core.util.service_exception import ServiceException
from rest_framework import status
from api.serializers.vistoria_serializer import VistoriaSerializer 
from api.serializers.vistoria_serializer import VistoriaCadastroSerializer
from api.serializers.vistoria_serializer import VistoriaAtualizacaoSerializer
from core.model.vistoria import Vistoria

def buscar_por_filtro(request: HttpRequest) -> List[Vistoria]:
    g_paginator = GenericPaginator(
        Vistoria,
        VistoriaSerializer
    )

    ordenacao = request.GET.get('ordenacao', None)

    filtro_data = request.GET.get('data', None)
    filtro_entrada = request.GET.get('entrada', None)
    filtro_saida = request.GET.get('saida', None)

    pag = request.GET.get('pag', None)
    max_reg_pag = request.GET.get('max_reg_pag', None)

    g_paginator.set_pag(pag)
    g_paginator.set_max_reg_pag(max_reg_pag)
    g_paginator.set_ordenacao(ordenacao)

    if filtro_data:
        g_paginator.queryset = g_paginator.queryset.filter(nome__icontains=filtro_data)

    if filtro_entrada:
        g_paginator.queryset = g_paginator.queryset.filter(entrada__icontains=filtro_entrada)

    if filtro_saida:
        g_paginator.queryset = g_paginator.queryset.filter(saida__icontains=filtro_saida)
        

    return g_paginator.get_objeto_para_view()

def buscar_por_id(id: int) -> Vistoria:
    try:
        vistoria = Vistoria.objects.get(pk=id)
        serializer = VistoriaSerializer(vistoria)

        return serializer.data
    except Vistoria.DoesNotExist:
        raise ServiceException(
            f'Vistoria de id:{id} não encontrada',
            status.HTTP_404_NOT_FOUND
        )

def criar(request: HttpRequest) -> Vistoria:
    serializer = VistoriaCadastroSerializer(data=request.data)

    if serializer.is_valid():

        entrada = serializer.validated_data.get('entrada')
        saida = serializer.validated_data.get('saida')

        if entrada == saida:
            raise ServiceException(
                "A entrada e a saída não podem ser iguais.",
                status.HTTP_400_BAD_REQUEST
            )

        vistoria = serializer.save()

        return vistoria.data
    else:
        raise ServiceException(serializer.errors, status.HTTP_400_BAD_REQUEST)



def atualizar(id: int,data):

    try:
        vistoria = Vistoria.objects.get(pk=id)
    except Vistoria.DoesNotExist:
        raise ServiceException(
            f'Vistoria de id:{id} não encontrada',
            status.HTTP_404_NOT_FOUND
        )

    serializer = VistoriaAtualizacaoSerializer(vistoria, data=data, partial=True)

    if serializer.is_valid():

        entrada = serializer.validated_data.get('entrada')
        saida = serializer.validated_data.get('saida')

        if entrada == saida:
            raise ServiceException(
                "A entrada e a saída não podem ser iguais.",
                status.HTTP_400_BAD_REQUEST
            )

        objeto_criado = serializer.save()
        return VistoriaSerializer(objeto_criado).data

    else:
        raise ServiceException(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

def remover(id: int) -> None:

    try:
        vistoria = Vistoria.objects.get(pk=id)
        vistoria.delete()
    except Vistoria.DoesNotExist:
        raise ServiceException(
            f'Vistoria de id:{id} não encontrada',
            status.HTTP_404_NOT_FOUND
        )

def remover_lista(ids: List[int]):
    if not ids:
        raise ServiceException(
            f'A lista precisa conter ao menos um elemento',
            status.HTTP_400_BAD_REQUEST)

    vistorias = Vistoria.objects.filter(id__in=ids) 

    if vistorias.exists():
        vistorias.delete()