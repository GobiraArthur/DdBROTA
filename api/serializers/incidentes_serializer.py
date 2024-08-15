from rest_framework import serializers
from core.model.incidentes import Incidentes

class IncidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = '__all__'

class IncidentesCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = [
            'tipo',
            'descricao'
        ]


class IncidentesAtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = [
            'tipo',
            'descricao',
        ]
