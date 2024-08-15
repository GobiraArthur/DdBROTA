from django.db import models

class Ocorrencia(models.Model):

    id = models.AutoField(primary_key=True)
    hora = models.TimeField()
    intinerario = models.CharField(max_length=60, blank=False)
    sentido = models.CharField(max_length=30, blank=False)
    ponto_referencia = models.CharField(max_length=60, blank=True)
    matricula_motorista = models.CharField(max_length=10, blank=False)
    matricula_cobrador = models.CharField(max_length=10, blank=True)

    descricao = models.TextField(
        blank=False
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.id} - {self.numero}'