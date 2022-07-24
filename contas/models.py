from tkinter import CASCADE
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=140)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome
    class Meta:
         ordering = ['dt_criacao']

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Transações'
        ordering =  ['categoria']
    