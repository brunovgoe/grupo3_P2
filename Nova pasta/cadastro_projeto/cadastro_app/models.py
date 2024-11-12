from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome_completo']

    def __str__(self):
        return self.username

class Aluno(models.Model):
    usuario = models.OneToOneField(UsuarioPersonalizado, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)  # Exemplo: adicione um campo específico de Aluno

    def __str__(self):
        return self.usuario.nome_completo

class Professor(models.Model):
    usuario = models.OneToOneField(UsuarioPersonalizado, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)  # Exemplo: adicione um campo específico de Professor

    def __str__(self):
        return self.usuario.nome_completo

class Instituicao(models.Model):
    usuario = models.OneToOneField(UsuarioPersonalizado, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18)  # Exemplo: adicione um campo específico de Instituição

    def __str__(self):
        return self.usuario.nome_completo

class Resposta(models.Model):
    texto = models.TextField()
    ordem = models.PositiveIntegerField()

    def __str__(self):
        return f"Resposta {self.ordem}: {self.texto[:50]}"

class QuestaoTeste(models.Model):
    enunciado = models.TextField()
    resposta_correta = models.ForeignKey(Resposta, on_delete=models.CASCADE, related_name='questoes')

    def __str__(self):
        return f"Questão: {self.enunciado[:50]}"
