# cadastro_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UsuarioPersonalizado, Professor, QuestaoTeste, Resposta, Curso, Aluno

# Formulário de criação do usuário personalizado para Aluno
class AlunoRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Email'})
    )
    nome_completo = forms.CharField(
        max_length=150,
        required=True,
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Nome Completo'})
    )
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control border-secondary'}),
        required=True,
        label='Curso'
    )
    
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'nome_completo', 'curso', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Nome de Usuário'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Confirmar Senha'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AlunoRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-secondary'
            if field_name in ['password1', 'password2']:
                field.widget = forms.PasswordInput(attrs={'class': 'form-control border-secondary', 'placeholder': field.label})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.nome_completo = self.cleaned_data['nome_completo']
        if commit:
            user.save()
            aluno = Aluno.objects.create(usuario=user, curso=self.cleaned_data['curso'])
            aluno.save()
        return user

# Formulário combinado para cadastro de Professor
class ProfessorRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Email'})
    )
    nome_completo = forms.CharField(
        max_length=150, 
        required=True, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Nome Completo'})
    )
    cursos = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        label='Cursos que o Professor Leciona'
    )
    
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'nome_completo', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Nome de Usuário'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Confirmar Senha'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfessorRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['cursos']:  # Evitar mudar estilo dos checkboxes
                field.widget.attrs['class'] = 'form-control border-secondary'
                if field_name in ['password1', 'password2']:
                    field.widget = forms.PasswordInput(attrs={'class': 'form-control border-secondary', 'placeholder': field.label})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.nome_completo = self.cleaned_data['nome_completo']
        if commit:
            user.save()
            professor = Professor.objects.create(usuario=user)
            professor.cursos.set(self.cleaned_data['cursos'])
            professor.save()
        return user

# Formulário para criar ou editar questões do teste
class QuestaoTesteForm(forms.ModelForm):
    class Meta:
        model = QuestaoTeste
        fields = ['enunciado', 'resposta_correta']
        widgets = {
            'enunciado': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'resposta_correta': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formulário para criar ou editar respostas
class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['aluno', 'questao_num', 'resposta', 'texto', 'ordem']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'questao_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'resposta': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Removida a classe InstituicaoForm
# class InstituicaoForm(forms.ModelForm):
#     class Meta:
#         model = Instituicao
#         fields = ['cnpj']
#         widgets = {
#             'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
#         }
