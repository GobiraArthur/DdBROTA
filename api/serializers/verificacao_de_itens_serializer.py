from rest_framework import serializers
from core.model.verificacao_de_itens import VerificacaoDeItens

class VerificacaoDeItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacaoDeItens
        fields = '__all__'

class VerificacaoDeItensCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacaoDeItens
        fields = ['nome']

class VerificacaoDeItensAtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacaoDeItens
        fields = ['nome', 'deletado_em']