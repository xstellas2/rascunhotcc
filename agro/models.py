from django.db import models

from django.utils.translation import gettext_lazy as _


class Sugestao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    sugestao = models.TextField()

    def __str__(self):
        return self.nome
    
class Agro(models.Model):
    localizacao = models.CharField(max_length=100)  # Exemplo de campo
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Exemplo de campo

    def __str__(self):
        return f"{self.localizacao} - {self.valor}"


class Praga(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(
        verbose_name=_("Descrição")
    )
    imagem = models.ImageField(
        verbose_name=_("Imagem"),
        upload_to='imagens/pragas/',  # pasta onde as imagens serão salvas
        null=True, 
        blank=True  # permite que o campo seja opcional
    )
    

    class Meta:
        verbose_name = _("Praga")
        verbose_name_plural = _("Pragas")

    def __str__(self):
        return f"{self.pk} | {self.nome} "
