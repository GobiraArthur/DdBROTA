from rest_framework import serializers
from core.model.ocorrencia import Ocorrencia

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'
class OcorrenciaCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = [
            'intinerario',
            'descricao',
            'ponto_referencia',
            'sentido',
            'matricula_motorista',
            'matricula_cobrador',
            'hora'
        ]

class OcorrenciaAtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = [
            'intinerario',
            'descricao',
            'ponto_referencia',
            'sentido',
            'matricula_motorista',
            'matricula_cobrador',
            'hora'
        ]