from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPersonalizado, Professor, Instituicao, QuestaoTeste, Resposta


class UsuarioPersonalizadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'nome_completo', 'curso', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['departamento']
        widgets = {
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['cnpj']
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        }


class QuestaoTesteForm(forms.ModelForm):
    class Meta:
        model = QuestaoTeste
        fields = ['enunciado', 'resposta_correta']


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['texto', 'ordem']
