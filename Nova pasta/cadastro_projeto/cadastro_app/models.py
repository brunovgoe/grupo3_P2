# cadastro_app/models.py
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    curso = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    disciplina = models.CharField(max_length=100)
    registro = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
