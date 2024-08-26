from django.db import models


class Sugestao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    sugestao = models.TextField()

    def __str__(self):
        return self.nome

# models.py
class Pesquisa(models.Model):
    praga = models.CharField(max_length=100)
    agrotoxico = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.praga
