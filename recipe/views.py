from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Verifique se o usuário está cadastrado
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('filter_recipe')  # Redirecione para a página de filtrar receitas
        else:
            # Usuário não cadastrado, retorne alguma página de erro ou mensagem
            return render(request, 'login_error.html')

    return render(request, 'login.html')

def register(request):
    return render(request, 'recipe/pages/cadastro.html')

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
