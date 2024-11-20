from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UsuarioPersonalizado(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    
    CURSO_CHOICES = [
        ('design', 'Design'),
        ('ciencia_computacao', 'Ciência da Computação'),
        ('sistemas_informacao', 'Sistemas de Informação'),
        ('ads', 'Análise e Desenvolvimento de Software (ADS)'),
        ('gestao_ti', 'Gestão de Tecnologia da Informação'),
    ]
    curso = models.CharField(max_length=50, choices=CURSO_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome_completo']
    
    def __str__(self):
        return self.username

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
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questao_num = models.PositiveIntegerField()
    resposta = models.CharField(max_length=255)
    texto = models.TextField()
    ordem = models.IntegerField()

    def __str__(self):
        return f"Usuário: {self.usuario}, Questão: {self.questao_num}, Resposta: {self.resposta}"
    
class QuestaoTeste(models.Model):
    enunciado = models.TextField()
    resposta_correta = models.ForeignKey(Resposta, on_delete=models.CASCADE, related_name='questoes')

    def __str__(self):
        return f"Questão: {self.enunciado[:50]}"
