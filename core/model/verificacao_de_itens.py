from django.db import models

class VerificacaoDeItens(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'