from rest_framework import serializers
from core.model.necessidades_de_manutencao import NecessidadeDeManutencao

class NecessidadesDeManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NecessidadeDeManutencao
        fields = '__all__' 

class NecessidadesDeManutencaoCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = NecessidadeDeManutencao
        fields = [
            'nome'
        ]

class NecessidadesDeManutencaoAtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NecessidadeDeManutencao
        fields = [
            'nome',
            'deletado_em'
        ]