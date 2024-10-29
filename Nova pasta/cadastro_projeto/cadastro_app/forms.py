# cadastro_app/forms.py
from django import forms
from .models import Aluno, Professor, Instituicao

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'curso', 'matricula']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'idade', 'disciplina', 'registro']

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome', 'endereco', 'telefone']
