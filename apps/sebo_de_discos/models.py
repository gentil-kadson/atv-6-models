from django.db import models

# Create your models here.

class SeloFonografico(models.Model):
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Artista(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Disco(models.Model):
    nome = models.TextField(max_length=200)
    descricao = models.TextField(max_length=300)
    selo_fonografico = models.ForeignKey(
        SeloFonografico, on_delete=models.CASCADE, related_name="discos")
    ano = models.IntegerField()
    pais = models.TextField(max_length=80)
    genero = models.TextField(max_length=70)
    quantidade = models.BigIntegerField()
    artistas = models.ManyToManyField(Artista)

    def __str__(self):
        return self.nome
