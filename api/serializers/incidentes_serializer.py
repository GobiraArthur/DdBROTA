from rest_framework import serializers
from api.serializers.ocorrencia_serializer import OcorrenciaAtualizacaoSerializer, OcorrenciaCadastroSerializer, OcorrenciaSerializer
from core.model.incidentes import Incidentes
from core.model.ocorrencia import Ocorrencia

class IncidentesSerializer(serializers.ModelSerializer):
    ocorrencia = OcorrenciaSerializer()
    class Meta:
        model = Incidentes
        fields = '__all__'

class IncidentesCadastroSerializer(serializers.ModelSerializer):
    ocorrencia = OcorrenciaCadastroSerializer(required=False, allow_null=True)
    class Meta:
        model = Incidentes
        fields = [
            'ocorrencia',
            'tipo',
            'descricao'
        ]

    def create(self, validated_data):
        ocorrencia_data = validated_data.pop('ocorrencia', None)  
        ocorrencia = None
    
        if ocorrencia_data:
            ocorrencia = Ocorrencia.objects.create(**ocorrencia_data) 
    
        incidente = Incidentes.objects.create(ocorrencia=ocorrencia, **validated_data)  
        return incidente
    
class IncidentesAtualizacaoSerializer(serializers.ModelSerializer):
    ocorrencia = OcorrenciaAtualizacaoSerializer(required=False, allow_null=True)
    class Meta:
        model = Incidentes
        fields = [
            'ocorrencia',
            'tipo',
            'descricao'
        ]

    def update(self, instance, validated_data):
        ocorrencia_data = validated_data.pop('ocorrencia', None)

        if ocorrencia_data:
            ocorrencia_instance = instance.ocorrencia
            for attr, value in ocorrencia_data.items():
                setattr(ocorrencia_instance, attr, value)
            ocorrencia_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
