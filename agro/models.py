from django.db import models

# Create your models here.

class Contato(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    telefone = models.CharField(max_length=155)
    sugestão = models.CharField(max_length=155)