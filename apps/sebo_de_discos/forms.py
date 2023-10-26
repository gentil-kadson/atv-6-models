from .models import Disco, Artista
from django.forms import ModelForm
from django import forms

class DiscoForm(ModelForm):
    class Meta:
        model = Disco
        fields = ['nome', 'descricao', 'selo_fonografico', 'ano', 'pais', 'genero', 'quantidade', 'artistas']