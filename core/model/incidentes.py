from django.db import models
from core.model.ocorencia import Ocorrencia

class Incidentes(models.Model):

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(
        max_length=50,
        blank=False
    )
    descricao =models.TextField(blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(null=True)
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.id} - {self.tipo}'