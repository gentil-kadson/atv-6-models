from django.shortcuts import render
from .models import Disco

# Create your views here.
def index(request):
    discos = Disco.objects.all()
    context = { 'discos': discos }

    return render(request, 'lista_discos.html', context)

