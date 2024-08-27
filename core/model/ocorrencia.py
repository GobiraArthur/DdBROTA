from django.db import models

class Ocorrencia(models.Model):

    id = models.AutoField(primary_key=True)
    hora = models.TimeField(null=True)
    intinerario = models.CharField(max_length=60, null=True)
    sentido = models.CharField(max_length=30, null=True)
    ponto_referencia = models.CharField(max_length=60, null=False)
    matricula_motorista = models.CharField(max_length=10, null=False)
    matricula_cobrador = models.CharField(max_length=10, null=True)
    descricao = models.TextField(null=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.id} - {self.numero}'