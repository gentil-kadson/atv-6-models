from django.db import models

# Create your models here.


class Disco(models.Model):
    nome = models.TextField(max_length=200)
    descricao = models.TextField(max_length=300)
    selo_fonografico = models.TextField(max_length=100)
    ano = models.IntegerField()
    pais = models.TextField(max_length=80)
    genero = models.TextField(max_length=70)
    quantidade = models.BigIntegerField()
