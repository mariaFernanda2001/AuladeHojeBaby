from django.db import models
from django.utils import timezone

# Create your models here.
class Coach(models.Model):
    nome = models.CharField(max_length=255, null=True)
    frase = models.TextField()
    inspirador = models.CharField(max_length=225, null=True)
    criado_em = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)

class Teste(models.Model):
    nome = models.CharField(max_length=25, null=True)
    idade = models.IntegerField(max_length=2)
    