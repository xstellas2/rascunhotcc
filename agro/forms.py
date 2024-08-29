from django import forms
from .models import Sugestao

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
