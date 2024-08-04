from typing import List
from api.serializers.telefone_emergencial_serializer import TelefoneEmergencialAtualizacaoSerializer, TelefoneEmergencialCadastroSerializer, TelefoneEmergencialSerializer
from core.model.telefone_emergencial import TelefoneEmergencial
from core.util.service_exception import ServiceException
from rest_framework import status


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