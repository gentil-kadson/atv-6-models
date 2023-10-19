from django.shortcuts import render
from .models import Disco, Artista, SeloFonografico

# Create your views here.
def index(request):
    discos = Disco.objects.all()
    context = { 'discos': discos }

    return render(request, 'lista_discos.html', context)

def disco(request, id_disco):
    disco = Disco.objects.get(id=id_disco)
    artistas = Artista.objects.filter(discos__id__in=[disco.id])

    context = { 'disco': disco, 'artistas': artistas }

    return render(request, 'detalhes_disco.html', context)

