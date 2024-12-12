from django.db import models

from django.utils.translation import gettext_lazy as _


class Sugestao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    sugestao = models.TextField()

    def __str__(self):
        return self.nome
    

from ckeditor.fields import RichTextField


class Praga(models.Model):
    nome = models.CharField(max_length=100)
    descricao = RichTextField(verbose_name="Descrição")  # Campo formatado
    imagem = models.ImageField(
        verbose_name="Imagem",
        upload_to='imagens/pragas/',
        null=True, 
        blank=True
    )
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    causas = RichTextField(blank=True, null=True)  # Campo formatado
    tratamento = RichTextField(blank=True, null=True)  # Campo formatado

    class Meta:
        ordering = ['nome']
        verbose_name = "Praga"
        verbose_name_plural = "Pragas"

    def __str__(self):
        return f"{self.pk} | {self.nome}"
