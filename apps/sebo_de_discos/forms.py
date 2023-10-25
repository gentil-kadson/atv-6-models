from .models import SeloFonografico
from django import forms

class DiscoForm(forms.Form):
    selos_fonograficos = SeloFonografico.objects.all()
    selos_fonograficos_tupla = []
    choice_number = 1

    for selo in selos_fonograficos:
        selos_fonograficos_tupla.append((choice_number, selo))
    
    selos_fonograficos_tupla = (selo for selo in selos_fonograficos_tupla)

    nome = forms.CharField(label="Título do disco", max_length=60)
    descricao = forms.CharField(label="Descrição", max_length=100)
    selo_fonografico = forms.ChoiceField(label="Selo fonográfico", choices=selos_fonograficos_tupla)
    ano = forms.IntegerField(label="Ano de lançamento")
    pais = forms.CharField(label="País de origem", max_length=30)
    genero = forms.CharField(label="Gênero", max_length=60)
    quantidade = forms.IntegerField(label="Quantidade")
