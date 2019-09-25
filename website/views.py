from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    if request.method =='POST':
       data = Coach()
       data.nome = request.POST['nome']
       data.frase = request.POST['frase']
       data.inspirador = request.POST['inspirador']
       data.save()
       contexto = {
           'mensagem': 'VOCÊ CONSEGUIU, GRITE ALUCINAÇÃO'
       }
       return render(request, 'index.html', contexto)

    return render(request, 'index.html')

def lista_coachs(request):
    lista_coachs = Coach.objects.all()
    args = {
        'lista' : listar_coachs
    }
    return reader(request, 'lista.html', contexto)