from rest_framework import serializers
from api.serializers.ocorrencia_serializer import OcorrenciaAtualizacaoSerializer, OcorrenciaCadastroSerializer, OcorrenciaSerializer
from core.model.incidentes import Incidentes

class IncidentesSerializer(serializers.ModelSerializer):
    ocorrencia = OcorrenciaSerializer()
    class Meta:
        model = Incidentes
        fields = '__all__'

class IncidentesCadastroSerializer(serializers.ModelSerializer):
    ocorrencia = OcorrenciaCadastroSerializer()
    class Meta:
        model = Incidentes
        fields = [
            'ocorrencia',
            'tipo',
            'descricao'
        ]
class IncidentesAtualizacaoSerializer(serializers.ModelSerializer):
    ocorrencia = OcorrenciaAtualizacaoSerializer()
    class Meta:
        model = Incidentes
        fields = [
            'ocorrencia',
            'tipo',
            'descricao',
        ]
