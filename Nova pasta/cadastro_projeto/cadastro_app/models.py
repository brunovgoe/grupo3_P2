# cadastro_app/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)  # Torna o email único para ser usado como USERNAME_FIELD

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def _str_(self):
        return self.nome_completo

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    usuario = models.OneToOneField(UsuarioPersonalizado, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.usuario.nome_completo

class Professor(models.Model):
    usuario = models.OneToOneField(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='professor')
    cursos = models.ManyToManyField(Curso)  # Relação Many-to-Many com Curso

    def __str__(self):
        return self.usuario.nome_completo

# Removido o modelo Instituicao

class Resposta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='respostas')  # Aluno que respondeu
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='respostas')  # Curso associado
    questao_num = models.PositiveIntegerField()
    resposta = models.CharField(max_length=255)
    texto = models.TextField()  # Campo texto
    ordem = models.IntegerField()  # Campo ordem
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Aluno: {self.aluno.usuario.username} - Curso: {self.curso.nome} - Questão: {self.questao_num}"

class QuestaoTeste(models.Model):
    enunciado = models.TextField()
    resposta_correta = models.CharField(max_length=255)  # Armazena a resposta correta como texto

    def __str__(self):
        return f"Questão: {self.enunciado[:50]}"
