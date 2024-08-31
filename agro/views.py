from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Pesquisa
from .models import Sugestao
from .forms import SugestaoForm

def salvar_sugestao(request):
    if request.method == 'POST':
        form = SugestaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agro:listar_sugestoes')  # Redireciona para a lista de sugestões após salvar
    else:
        form = SugestaoForm()
    return render(request, 'formulario.html', {'form': form})


def deletar_sugestao(request, pk):
    print(pk)
    sugestao = get_object_or_404(Sugestao, pk=pk)
    sugestao.delete()
    
    messages.success(request, 'Sugestão deletada com sucesso!')
    return redirect('agro:listar_sugestoes')  

def editar_sugestao(request, pk):
    sugestao = get_object_or_404(Sugestao, pk=pk)
    if request.method == 'POST':
        form = SugestaoForm(request.POST, instance=sugestao)
        if form.is_valid():
            form.save()
            return redirect('agro:listar_sugestoes')
    else:
        form = SugestaoForm(instance=sugestao)
    return render(request, 'editar_sugestoes.html', {'form': form})

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
    query = request.GET.get('query', '')  # Pega a consulta, ou uma string vazia se não houver
    results = []

    if query:
        results = Pesquisa.objects.filter(praga__icontains=query)  # Pesquisa pelo campo `praga`

    return render(request, 'search_results.html', {'results': results, 'query': query})



