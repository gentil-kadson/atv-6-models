from .models import Disco
from django.forms import ModelForm

class DiscoForm(ModelForm):
    class Meta:
        model = Disco
        fields = ['nome', 'descricao', 'selo_fonografico', 'ano', 'pais', 'genero', 'quantidade', 'artistas']