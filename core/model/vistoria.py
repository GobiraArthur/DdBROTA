from django.db import models
from core.model.incidentes import Incidentes
from core.model.necessidades_de_manutencao import NecessidadeDeManutencao
from core.model.verificacao_de_itens import VerificacaoDeItens

class Vistoria(models.Model):
    data = models.DateTimeField(auto_now_add=False, null=False) 
    entrada = models.DateTimeField(null=False, auto_now_add=False) 
    saida = models.DateTimeField(null=False, auto_now_add=False)
    motorista = models.CharField(max_length=200, blank=False)
    veiculo = models.CharField(max_length=200, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.data}'


class VistoriaIncidente(models.Model):
    vistoria = models.ForeignKey(Vistoria, on_delete=models.CASCADE, related_name='incidentes')
    incidente = models.ForeignKey('Incidentes', on_delete=models.CASCADE)

    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['vistoria', 'incidente'], 
            name='unique_vistoria_incidente')]


class VistoriaNecessidadeManutencao(models.Model):
    vistoria = models.ForeignKey(Vistoria, on_delete=models.CASCADE, related_name='necessidades_manutencao')
    necessidade_manutencao = models.ForeignKey('NecessidadeDeManutencao', on_delete=models.CASCADE)

    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['vistoria', 'necessidade_manutencao'], 
            name='unique_vistoria_necessidade_manutencao')]


class VistoriaVerificacaoItens(models.Model):
    STATUS_CHOICES = [
        ('C', 'C'),
        ('NC', 'NC'),
        ('NA', 'NA')
    ]
    vistoria = models.ForeignKey(Vistoria, on_delete=models.CASCADE, related_name='itens_verificados')  
    verificacao_itens = models.ForeignKey('VerificacaoDeItens', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    class Meta: 
        constraints = [
            models.UniqueConstraint(fields=['vistoria', 'verificacao_itens'], 
            name='unique_vistoria_verificacao_itens')]

    def __str__(self):
        return f"Vistoria {self.vistoria.id} - Item {self.verificacao_itens.nome}: {self.status}"

