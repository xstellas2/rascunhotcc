from django import forms
from .models import Sugestao
from django import forms
from agro.models import Praga


class SugestaoForm(forms.ModelForm):
    class Meta:
        model = Sugestao
        fields = ['nome', 'email', 'telefone', 'sugestao']
        widgets = {
            'sugestao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }



class AgroForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome da praga",
        })
    )
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Descrição da praga",
            "rows": 4,
        })
    )
    imagem = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "form-control-file",
        }),
        required=True 
    )
    

    class Meta:
        model = Praga
        fields = (
            "nome",
            "descricao",
            "imagem",
        )
