from typing import List

from django.http import HttpRequest
from api.serializers.telefone_emergencial_serializer import TelefoneEmergencialAtualizacaoSerializer, TelefoneEmergencialCadastroSerializer, TelefoneEmergencialSerializer
from core.model.telefone_emergencial import TelefoneEmergencial
from core.util.generic_paginator import GenericPaginator
from core.util.service_exception import ServiceException
from rest_framework import status

def buscar_por_filtro(request: HttpRequest) -> List[TelefoneEmergencial]:

    g_paginator = GenericPaginator(
        TelefoneEmergencial,
        TelefoneEmergencialSerializer
    )

    ordenacao = request.GET.get('ordenacao', None)

    filtro_numero = request.GET.get('numero', None)
    filtro_descricao = request.GET.get('descricao', None)
    
    pag = request.GET.get('pag', None)
    max_reg_pag = request.GET.get('max_reg_pag', None)

    g_paginator.set_pag(pag)
    g_paginator.set_max_reg_pag(max_reg_pag)
    g_paginator.set_ordenacao(ordenacao)
    
    if filtro_numero:
        g_paginator.queryset = g_paginator.queryset.filter(numero__startswith=filtro_numero)

    if filtro_descricao:
        g_paginator.queryset = g_paginator.queryset.filter(descricao__icontains=filtro_descricao)

    return g_paginator.get_objeto_para_view()

def buscar_por_id(id: int) -> TelefoneEmergencial:
    try:
        telefone = TelefoneEmergencial.objects.get(pk=id)
        serializer = TelefoneEmergencialSerializer(telefone)

        return serializer.data
    except TelefoneEmergencial.DoesNotExist:
        raise ServiceException(
            f'Telefone emergencial de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )

def criar(data):

    serializer = TelefoneEmergencialCadastroSerializer(
        data=data
    )

    if serializer.is_valid():

        if TelefoneEmergencial.objects.filter(
            numero=serializer.validated_data.get('numero')
        ).exists():
            raise ServiceException(
                f'Telefone emergencial já cadastrado!',
                status.HTTP_400_BAD_REQUEST
            )

        objeto_criado = serializer.save()

        return TelefoneEmergencialSerializer(objeto_criado).data
    else:
        raise ServiceException(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

def atualizar(id:int,data):

    try:
        telefone = TelefoneEmergencial.objects.get(pk=id)
    except TelefoneEmergencial.DoesNotExist:
        raise ServiceException(
            f'Telefone emergencial de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )
    
    serializer = TelefoneEmergencialAtualizacaoSerializer(
        telefone,
        data=data,
        partial=True
    )

    if serializer.is_valid():

        if TelefoneEmergencial.objects.exclude(pk=id).filter(
            numero=serializer.validated_data.get('numero')
        ).exists():
            raise ServiceException(
                f'Telefone emergencial já cadastrado!',
                status.HTTP_400_BAD_REQUEST
            )

        objeto_criado = serializer.save()

        return TelefoneEmergencialSerializer(objeto_criado).data
    else :
        raise ServiceException(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

def remover(id:int):

    try:
        telefone = TelefoneEmergencial.objects.get(pk=id)
        
        telefone.delete()
    except TelefoneEmergencial.DoesNotExist:
        raise ServiceException(
            f'Telefone emergencial de id:{id} não encontrado',
            status.HTTP_404_NOT_FOUND
        )

def remover_lista(ids: List[int]):
    if not ids:
        raise ServiceException(
            f'A lista precisa conter ao menos um elemento',
            status.HTTP_400_BAD_REQUEST
        )
    
    telefones = TelefoneEmergencial.objects.filter(id__in=ids) 

    if telefones.exists():
        telefones.delete()