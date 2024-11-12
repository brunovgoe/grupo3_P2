from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPersonalizado, Aluno, Professor, Instituicao, QuestaoTeste, Resposta

# Formulário de criação do usuário personalizado
class UsuarioPersonalizadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'nome_completo', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

# Formulário de alteração do usuário personalizado
class UsuarioPersonalizadoChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'nome_completo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário específico para aluno
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['curso']  # Inclua apenas campos específicos de Aluno

# Formulário específico para professor
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['departamento']
        widgets = {
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário específico para instituição
class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['cnpj']
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário para criar ou editar questões do teste
class QuestaoTesteForm(forms.ModelForm):
    class Meta:
        model = QuestaoTeste
        fields = ['enunciado', 'resposta_correta']

# Formulário para criar ou editar respostas
class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['texto', 'ordem']
