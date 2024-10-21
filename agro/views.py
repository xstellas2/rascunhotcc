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


# Create your views here.
class AgroListView(LoginRequiredMixin, generic.ListView):
    model = Agro
    paginate_by = 5

class AgroDetailView(LoginRequiredMixin, generic.DetailView):
    model = Agro

class AgroCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Agro
    form_class = AgroForm
    success_url = reverse_lazy("agro:agro-list")
    success_message = "agro cadastrado com sucesso!"


class AgroUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Agro
    form_class = AgroForm
    success_url = reverse_lazy("agro:agro-list")
    success_message = "agro atualizada com sucesso!"

class AgroDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Agro
    success_url = reverse_lazy("agro:agro-list")
    success_message = "agro excluído com sucesso!"


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Substitua 'home' pela URL de redirecionamento desejada
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


