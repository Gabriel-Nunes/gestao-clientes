from django.shortcuts import render, redirect
from django.contrib.auth import logout


# View para renderização da página inicial.
# o usuário não precisa estar logado
def home(request):
    return render(request, 'home.html')


# Faz o logout do usuário e redireciona para a home
def user_logout(request):
    logout(request)
    return redirect('home')
