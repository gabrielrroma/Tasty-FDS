from django.shortcuts import render

def login(request):
    return render(request,'recipe/login.html')

def register(request):
    return render(request, 'recipe/cadastro.html')

def filtrarreceita(request):
    return render(request, 'recipe/filtrarreceita.html')

def novareceita(request):
    return render(request, 'recipe/novareceita.html')

def historico(request):
    return render(request, 'recipe/historico.html')

def perfil(request):
    return render(request, 'recipe/perfil.html')

def recomendacoes(request):
    return render(request, 'recipe/recomendacoes.html')
