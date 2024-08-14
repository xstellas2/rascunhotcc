from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def lagartas(request):
    return render(request, 'lagartas.html')

def agrotoxico(request):
    return render(request, 'agrotoxico.html')

def gafanhotos(request):
    return render(request, 'gafanhotos.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def listagem_sugestoes(request):
    return render(request, 'listagem_sugestoes.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')