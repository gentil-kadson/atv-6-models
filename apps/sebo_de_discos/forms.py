# from .models import SeloFonografico, Artista
# from django import forms

# class DiscoForm(forms.Form):
#     # tratando os selos para o select
#     selos_fonograficos = SeloFonografico.objects.all()
#     selos_fonograficos_tupla = []
#     n_da_opcao = 1

#     for selo in selos_fonograficos:
#         selos_fonograficos_tupla.append((n_da_opcao, selo))
#         n_da_opcao += 1
    
#     selos_fonograficos_tupla = (selo for selo in selos_fonograficos_tupla)

#     # tratando os artistas para o select
#     artistas = Artista.objects.all()
#     artistas_tupla = []

#     for artista in artistas:
#         artistas_tupla.append((artista, f'{artista.nome}'))
    
#     artistas_tupla = (artista for artista in artistas_tupla)

#     nome = forms.CharField(label="Título do disco", max_length=60)
#     descricao = forms.CharField(label="Descrição", max_length=100)
#     selo_fonografico = forms.ChoiceField(label="Selo fonográfico", choices=selos_fonograficos_tupla)
#     ano = forms.IntegerField(label="Ano de lançamento")
#     pais = forms.CharField(label="País de origem", max_length=30)
#     genero = forms.CharField(label="Gênero", max_length=60)
#     quantidade = forms.MultipleChoiceField(label="Artista(s)", choices=artistas_tupla)
