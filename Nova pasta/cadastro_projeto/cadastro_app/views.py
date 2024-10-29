# cadastro_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlunoForm, ProfessorForm, InstituicaoForm

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('cadastrar_aluno')
    else:
        form = AlunoForm()
    return render(request, 'cadastro_app/cadastrar_aluno.html', {'form': form})

def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor cadastrado com sucesso!')
            return redirect('cadastrar_professor')
    else:
        form = ProfessorForm()
    return render(request, 'cadastro_app/cadastrar_professor.html', {'form': form})

def cadastrar_instituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instituição cadastrada com sucesso!')
            return redirect('cadastrar_instituicao')
    else:
        form = InstituicaoForm()
    return render(request, 'cadastro_app/cadastrar_instituicao.html', {'form': form})
