from django.shortcuts import render
from django.db.models import Q
from .models import Sugestao
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Pesquisa

def editar_sugestao(request, id):
    sugestao = get_object_or_404(Sugestao, id=id)
    if request.method == "POST":
        sugestao.nome = request.POST.get('nome')
        sugestao.email = request.POST.get('email')
        sugestao.telefone = request.POST.get('telefone')
        sugestao.sugestao = request.POST.get('sugestao')
        sugestao.save()
        
        messages.success(request, 'Sugestão atualizada com sucesso!')
        return redirect('listar_sugestoes')

    return render(request, 'editar_sugestao.html', {'sugestao': sugestao})

def deletar_sugestao(request, id):
    sugestao = get_object_or_404(Sugestao, id=id)
    sugestao.delete()
    
    messages.success(request, 'Sugestão deletada com sucesso!')
    return redirect('listar_sugestoes')


def salvar_sugestao(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        sugestao = request.POST.get('sugestao')

        if nome and email and sugestao:  # Verifica se os campos obrigatórios estão preenchidos
            Sugestao.objects.create(nome=nome, email=email, telefone=telefone, sugestao=sugestao)
            messages.success(request, 'Sugestão enviada com sucesso!')
        else:
            messages.error(request, 'Preencha todos os campos obrigatórios.')

        return redirect('listar_sugestoes')

    return render(request, 'formulario.html')


def listar_sugestoes(request):
    contato = Sugestao.objects.all()  # Recupera todas as sugestões
    return render(request, 'listagem_sugestoes.html', {'contato': contato, 'messages': messages.get_messages(request)})

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

def formulario(request):
    return render(request, 'formulario.html')

def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Pesquisa.objects.filter(praga__icontains=query)  # Pesquisa pelo título
    return render(request, 'search_results.html', {'results': results, 'query': query})




def deletar_sugestao(request):
    return render(request, 'deletar_sugestao.html')

def editar_sugestoes(request):
    return render(request, 'editar_sugestoes.html')

