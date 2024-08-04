from rest_framework import serializers
from core.model.telefone_emergencial import TelefoneEmergencial

class TelefoneEmergencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneEmergencial
        fields = '__all__'

class TelefoneEmergencialCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneEmergencial
        fields = [
            'numero'
        ]

class TelefoneEmergencialAtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneEmergencial
        fields = [
            'numero'
        ]