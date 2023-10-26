from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render (request,'recipe/login.html')

def register(request):
    return render(request, 'recipe/cadastro.html')

def filtrarreceita(request):
    return render (request, 'recipe/filtrarreceita.html')

def novareceita(request):
    return render(request, 'recipe/novareceita.html')

def historico(request):
    return render(request, 'recipe/historico.html')
