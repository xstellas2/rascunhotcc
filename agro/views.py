from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Sugestao
from .forms import SugestaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from .forms import AgroForm
from .models import Agro
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from .models import Praga

# View para cadastro de nova praga
@login_required
def nova_praga(request):
    if request.method == 'POST':
        form = AgroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redireciona para a página de listagem após o cadastro
            return redirect('agro:agro_list')
    else:
        form = AgroForm()
    
    return render(request, 'agro/nova_praga.html', {'form': form})

# View para listar as pragas cadastradas
@login_required
def agro_list(request):
    pragas = Praga.objects.all()  # Lista todas as pragas
    return render(request, 'agro/agro_list.html', {'pragas': pragas})




def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('agro:nova_praga')  
            else:
                messages.error(request, "Nome de usuário ou senha inválidos.")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



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


