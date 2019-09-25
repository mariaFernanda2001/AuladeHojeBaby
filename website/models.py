from django.db import models
from django.utils import timezone

# Create your models here.
class Coach(models.Model):
    nome = models.CharField(max_length=255, null=True)
    frase = models.TextField()
    inspirador = models.CharField(max_length=225, null=True)
    
    criado_em = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __Str__(self):
        return self.nome