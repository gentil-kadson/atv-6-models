from django.shortcuts import render, HttpResponseRedirect
from .models import Disco, Artista
from .forms import DiscoForm


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

def cadastrar_disco(request):
    if request.method == "POST":
        form_cadastro_disco = DiscoForm(request.POST)

        if form_cadastro_disco.is_valid():
            Disco.save(form_cadastro_disco)
            return HttpResponseRedirect("/")
    else:
        form_cadastro_disco = DiscoForm()

    return render(request, 'cadastrar_disco.html', { 'form': form_cadastro_disco })