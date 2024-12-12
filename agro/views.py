from django.shortcuts import get_object_or_404
from .models import Sugestao
from .forms import SugestaoForm
from .forms import AgroForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Praga
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .forms import UserCreationForm


def agro_list(request):
    nome = request.GET.get('nome', '')
    descricao = request.GET.get('descricao', '')
    pragas = Praga.objects.all().order_by('nome')

    if nome:
        pragas = pragas.filter(nome__icontains=nome)

    paginator = Paginator(pragas, 9)  # 9 itens por página
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)

    return render(request, 'agro/agro_list.html', {'page_obj': page_obj, 'nome': nome, 'descricao': descricao})

def like_praga(request, praga_id):
    praga = Praga.objects.get(id=praga_id)
    praga.likes += 1
    praga.save()
    return JsonResponse({'likes': praga.likes, 'dislikes': praga.dislikes})

def dislike_praga(request, praga_id):
    praga = Praga.objects.get(id=praga_id)
    praga.dislikes += 1
    praga.save()
    return JsonResponse({'likes': praga.likes, 'dislikes': praga.dislikes})

def agro_deletar(request, pk):
    praga = get_object_or_404(Praga, pk=pk) 
    praga.delete()  # Deleta a praga
    
    return redirect('agro:agro_list')  

def agro_editar(request, pk):
    praga = get_object_or_404(Praga, pk=pk)  
    if request.method == 'POST':
        form = AgroForm(request.POST, request.FILES, instance=praga)  # Inclui request.FILES para lidar com imagens
        if form.is_valid():
            form.save()  
            return redirect('agro:agro_detalhe', praga_id=pk)   
    else:
        form = AgroForm(instance=praga)  
    return render(request, 'agro/agro_editar.html', {'form': form, 'praga': praga})


def agro_detalhe(request, praga_id):
    praga = get_object_or_404(Praga, id=praga_id)
    return render(request, 'agro/agro_detalhe.html', {'praga': praga})

@login_required
def nova_praga(request):
    if request.method == 'POST':
        form = AgroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redireciona para a página de listagem após o cadastro
            return redirect('/agro_list/')
    else:
        form = AgroForm()
    
    return render(request, 'agro/nova_praga.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('agro:index')  # Certifique-se de usar o nome da rota correto
            else:
                messages.error(request, "Nome de usuário ou senha inválidos.")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def cadastrar(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password1')
            senha2 = form.cleaned_data.get('password2')
            user = User.objects.filter(username=username).first()
            print(user)
            if (user is None):
                print('oi')
                if (senha == senha2):
                    user = User.objects.create_user(username=username, password=senha)
                    user.save()
                    return redirect('agro:custom_login')
                else:
                    messages.warning(request, "As senhas não coincidem.")
            else:
                messages.warning(request, "Nome de usuário ou senha inválidos.")
    return render(request, 'cadastrar.html', context={'form': form})


@login_required
def salvar_sugestao(request):
    if request.method == 'POST':
        form = SugestaoForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensagem de sucesso
            return redirect('agro:index')  
    else:
        form = SugestaoForm()

    return render(request, 'formulario.html', {'form': form})


def deletar_sugestao(request, pk):
    print(pk)
    sugestao = get_object_or_404(Sugestao, pk=pk)
    sugestao.delete()
    
    messages.success(request, 'Sugestão deletada com sucesso!')
    return redirect('agro:listar_sugestoes')  

def listar_sugestoes(request):
    contato = Sugestao.objects.all()  # Recupera todas as sugestões
    return render(request, 'listagem_sugestoes.html', {'contato': contato, 'messages': messages.get_messages(request)})

def index(request):
    pragas = Praga.objects.all()
    return render(request, 'index.html', {'pragas': pragas})

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

def sair(request):
    logout(request)
    return redirect('/')