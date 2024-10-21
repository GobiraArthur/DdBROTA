from rest_framework import serializers
from core.model.vistoria import Vistoria, VistoriaIncidente, VistoriaNecessidadeManutencao, VistoriaVerificacaoItens
from core.model.ocorrencia import Ocorrencia
from core.model.incidentes import Incidentes
from core.model.necessidades_de_manutencao import NecessidadeDeManutencao
from core.model.verificacao_de_itens import VerificacaoDeItens


class OcorrenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ocorrencia
        fields = '__all__'

class VistoriaIncidenteSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='incidente.tipo')
    descricao = serializers.CharField(source='incidente.descricao')
    ocorrencia = OcorrenciaSerializer(source = 'incidente.ocorrencia', required=False)

    class Meta:
        model = VistoriaIncidente
        fields = ['tipo','descricao','ocorrencia']  

class IncidenteSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(required=True)  
    descricao = serializers.CharField(required=True) 
    ocorrencia = OcorrenciaSerializer(required=False)

    class Meta:
        model = Incidentes  
        fields = ['tipo', 'descricao', 'ocorrencia'] 


class VistoriaNecessidadeManutencaoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='necessidade_manutencao.nome')

    class Meta:
        model = VistoriaNecessidadeManutencao
        fields = ['nome']

class NecessidadeManutencaoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(required=True)  

    class Meta:
        model = NecessidadeDeManutencao
        fields = ['nome'] 

class VistoriaItensVerificadosSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='verificacao_itens.nome')  
    status = serializers.ChoiceField(choices=VistoriaVerificacaoItens.STATUS_CHOICES)

    class Meta:
        model = VistoriaVerificacaoItens
        fields = ['nome', 'status']

class VistoriaSerializer(serializers.ModelSerializer):
    
    incidentes = VistoriaIncidenteSerializer(many=True)
    necessidades_manutencao = VistoriaNecessidadeManutencaoSerializer(many=True)
    itens_verificados = VistoriaItensVerificadosSerializer(many=True)

    class Meta:
        model = Vistoria
        fields = '__all__'  

class VistoriaCadastroSerializer(serializers.ModelSerializer):

    incidentes = IncidenteSerializer(many=True, allow_null=True, required=False)
    necessidades_manutencao = NecessidadeManutencaoSerializer(many=True, required=False)
    itens_verificados = VistoriaItensVerificadosSerializer(many=True, required=False)

    class Meta:
        model = Vistoria
        fields = '__all__'

    def create(self, validated_data):
        
        incidentes_data = validated_data.pop('incidentes', None)
        necessidades_manutencao_data = validated_data.pop('necessidades_manutencao', None)
        itens_verificados_data = validated_data.pop('itens_verificados', None)

        vistoria = Vistoria.objects.create(**validated_data)

        
        for incidente_data in incidentes_data:
            tipo = incidente_data.get('tipo')  
            descricao = incidente_data.get('descricao')  

            ocorrencia_data = incidente_data.get('ocorrencia', None)
            ocorrencia = None
            if ocorrencia_data:
                ocorrencia, created = Ocorrencia.objects.get_or_create(**ocorrencia_data)

            incidente, created = Incidentes.objects.get_or_create(
                tipo=tipo,
                descricao=descricao,
                ocorrencia=ocorrencia)
            VistoriaIncidente.objects.create(vistoria=vistoria, incidente=incidente)

        
        for necessidade_data in necessidades_manutencao_data:
            nome = necessidade_data.get('nome')
            
            necessidade, created = NecessidadeDeManutencao.objects.get_or_create(nome=nome)
            VistoriaNecessidadeManutencao.objects.create(vistoria=vistoria, necessidade_manutencao=necessidade)

        
        for item_data in itens_verificados_data:
            nome = item_data.get('verificacao_itens')['nome']
            status = item_data.get('status')

            item, created = VerificacaoDeItens.objects.get_or_create(nome=nome)
            VistoriaVerificacaoItens.objects.create(vistoria=vistoria, verificacao_itens=item, status=status)

        return vistoria 


class VistoriaAtualizacaoSerializer(serializers.ModelSerializer):
    
    incidentes = VistoriaIncidenteSerializer (many=True, allow_null=True, required=False, read_only=False)
    necessidades_manutencao = VistoriaNecessidadeManutencaoSerializer(many=True, required=False, read_only=False)
    itens_verificados = VistoriaItensVerificadosSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = Vistoria
        fields = '__all__'
   

    def update(self, instance, validated_data):

        incidentes_data = validated_data.pop('incidentes', None)
        necessidades_manutencao_data = validated_data.pop('necessidades_manutencao', None)
        itens_verificados_data = validated_data.pop('itens_verificados', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        
        if incidentes_data:
            for incidente_data in incidentes_data:
                
                vistoria_incidente = VistoriaIncidente.objects.filter(vistoria=instance).first()

                if vistoria_incidente:
                    incidente = vistoria_incidente.incidente

                    tipo = incidente_data.get('incidente', {}).get('tipo')
                    descricao = incidente_data.get('incidente', {}).get('descricao')

                    incidente.tipo = tipo
                    incidente.descricao = descricao

                    ocorrencia_data = incidente_data.get('incidente', {}).get('ocorrencia')

                    if ocorrencia_data:
                        if incidente.ocorrencia:
                            id_ocorrencia = incidente.ocorrencia.id

                            Ocorrencia.objects.filter(id=id_ocorrencia).update(**ocorrencia_data)
                        else:
                            nova_ocorrencia = Ocorrencia.objects.create(**ocorrencia_data)
                            
                            incidente.ocorrencia = nova_ocorrencia
                            
                    else:
                        incidente.ocorrencia = None

                    incidente.save()
                    VistoriaIncidente.objects.update_or_create(vistoria=instance, incidente=incidente)
                
        if necessidades_manutencao_data:
            instance.necessidades_manutencao.all().delete()

            for necessidade_data in necessidades_manutencao_data:

                nome = necessidade_data.get('necessidade_manutencao').get('nome')
                
                necessidades = NecessidadeDeManutencao.objects.filter(nome=nome)

                for necessidade in necessidades:
                    necessidade.nome = nome
                    necessidade.save()

                VistoriaNecessidadeManutencao.objects.update_or_create(vistoria=instance, necessidade_manutencao=necessidade)

        if itens_verificados_data:
            instance.itens_verificados.all().delete()

            for item_data in itens_verificados_data:
                nome = item_data.get('verificacao_itens').get('nome')
                status = item_data.get('status')

                itens = VerificacaoDeItens.objects.filter(nome=nome)

                for item in itens:
                    item.nome = nome  
                    item.save()

                    VistoriaVerificacaoItens.objects.update_or_create(
                        vistoria=instance,
                        verificacao_itens=item,
                        defaults={'status': status})

        instance.save() 
        return instance
