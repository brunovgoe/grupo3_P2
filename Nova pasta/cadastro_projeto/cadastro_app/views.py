# cadastro_app/views.py

from .forms import ProfessorRegistrationForm, AlunoRegistrationForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from .models import Resposta, Professor, Aluno, UsuarioPersonalizado
from django.contrib.auth import get_user_model
from django import forms

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

def pagina_inicial(request):
    return render(request, 'cadastro_app/escolha_perfil.html')  # Atualizado para 'escolha_perfil'

def inicio_aluno(request):
    return render(request, 'cadastro_app/inicio_aluno.html')

def inicio_professor(request):
    return render(request, 'cadastro_app/inicio_professor.html')

# Removido a função inicio_instituicao

@login_required
def home(request):
    resumo_lido = request.session.get('resumo_lido', False)
    return render(request, 'cadastro_app/home.html', {'resumo_lido': resumo_lido})

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso! Por favor, faça o login.')
            return redirect('login_aluno')
        else:
            messages.error(request, 'Houve um erro no cadastro. Verifique as informações.')
    else:
        form = AlunoRegistrationForm()
    return render(request, 'cadastro_app/cadastrar_aluno.html', {'form': form})

def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor cadastrado com sucesso! Por favor, faça o login.')
            return redirect('login_professor')
        else:
            messages.error(request, 'Houve um erro no cadastro. Verifique as informações.')
    else:
        form = ProfessorRegistrationForm()
    return render(request, 'cadastro_app/cadastrar_professor.html', {'form': form})

# Removido completamente a função cadastrar_instituicao

def resumo_pbl(request):
    return render(request, 'cadastro_app/resumo_pbl.html')

def confirmar_leitura(request):
    if request.method == 'POST':
        request.session['resumo_lido'] = True
        request.session.modified = True
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@login_required
def teste_pbl(request):
    if not request.session.get('resumo_lido', False):
        return HttpResponseForbidden("Você precisa ler o resumo antes de fazer o teste.")
    return render(request, 'cadastro_app/teste_pbl.html')

def teste_pbl_questao(request, questao_num):
    questoes = [
        {
            'pergunta': "PROBLEMA(S) DO CLIENTE COMO PROPOSTA EDUCACIONAL",
            'opcoes': [
                "As atividades de aprendizagem (conteúdo, práticas, exercícios) são ministradas independentemente do problema.",
                "Todas as atividades são iniciadas, motivadas e direcionadas para a resolução de uma tarefa ou problema específico, sendo este o propósito maior de aprendizagem.",
                "Nem todas as atividades estão associadas com a resolução de tarefas ou problemas específicos. Por exemplo, o conteúdo é explanado sem relação com a prática.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "O ALUNO SENTE-SE RESPONSÁVEL PELA RESOLUÇÃO DO PROBLEMA",
            'opcoes': [
                "Postura totalmente passiva com relação ao problema.",
                "O aluno se envolve com o problema para cumprir metas, geralmente na entrega de resultados parciais exigidos pelo professor ou tutor.",
                "O aluno está totalmente envolvido com o problema, demonstrando engajamento na busca pela sua solução, independente de tarefas exigidas pelo professor ou tutor.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "AUTENTICIDADE DO PROBLEMA OU TAREFA",
            'opcoes': [
                "As tarefas de aprendizagem não refletem as situações do mundo real.",
                "As tarefas de aprendizagem são reais, definidas e acompanhadas a partir de clientes reais, em contexto real controlado por escopo da solução, prazos de entrega e esforço despendido.",
                "Problema ou tarefa real, mas sem a participação do cliente ou ainda definição do contexto realizada pelo professor.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "AUTENTICIDADE DO AMBIENTE DE APRENDIZAGEM",
            'opcoes': [
                "O ambiente de aprendizado é convencional, tanto o físico (mobília e recursos) quanto os procedimentos.",
                "O ambiente de aprendizado é real, com os mesmos desafios que você encontrará no ambiente de trabalho para o qual está sendo treinado: equipe, infraestrutura e processos reais.",
                "O ambiente de aprendizado é uma simulação do mundo real.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "CONDUÇÃO DO PROCESSO DE RESOLUÇÃO DO PROBLEMA",
            'opcoes': [
                "O processo de resolução do problema é totalmente conduzido pelo professor ou tutor, sem entendimento por parte do aluno.",
                "O professor ou tutor define o processo de resolução do problema, mas o aluno o entende, sabe aplicá-lo e é capaz de identificar pontos fortes e de melhoria.",
                "O aluno define o processo de resolução de problema, descrevendo suas etapas, pontos fortes e de melhoria.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "COMPLEXIDADE DO PROBLEMA OU TAREFA",
            'opcoes': [
                "Os problemas ou tarefas são simples de resolver, exigindo pouco do assunto abordado na disciplina.",
                "A complexidade dos problemas ou tarefas é moderada, por não exigir muito esforço do aluno na busca de informações ou soluções alternativas para sua resolução.",
                "A complexidade do problema ou tarefa estimula o raciocínio e o desafio no desenvolvimento das ideias acerca do problema proposto. São necessárias mais informações que as fornecidas para entender o problema e conhecer as ações necessárias para a sua solução.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "AVALIAÇÃO E ANÁLISE DA SOLUÇÃO PARA O PROBLEMA",
            'opcoes': [
                "A solução para o problema é proposta por um dos membros da equipe, a partir de seu conhecimento e/ou experiência individual.",
                "Soluções são propostas por um ou mais alunos e, a partir da discussão entre os membros do grupo, decide-se pela melhor solução.",
                "As soluções são construídas a partir de um processo investigativo e questionador de ideias entre os membros da equipe, que buscam novas fontes e contextos alternativos para desenvolver a melhor solução para o problema.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "REFLEXÃO SOBRE COMO O ALUNO APRENDEU O CONTEÚDO NO PROCESSO DE APRENDIZAGEM",
            'opcoes': [
                "O aluno não tem oportunidade para refletir sobre sua aprendizagem.",
                "O aluno tem oportunidade para refletir sobre sua aprendizagem, mas não é orientado para o desenvolvimento de habilidades de autorreflexão sobre o processo de construção do conhecimento. Por exemplo, não é orientado a identificar e descrever como aprendeu, o que aprendeu e o que precisa aprender.",
                "O aluno tem oportunidade de pensar e agir reflexivamente, demonstrando habilidades de autorreflexão, descrevendo como aprendeu, o que aprendeu e o que precisa aprender. Do aluno é exigido que descreva as etapas de resolução do problema e o planejamento do processo de resolução.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "FORMA DE APRENDIZAGEM",
            'opcoes': [
                "A aprendizagem ocorre em grupos, mas há pouca colaboração e interatividade (participação) com os colegas do grupo, também como para os professores e tutores.",
                "A aprendizagem é colaborativa e acontece através de várias direções entre (professor - aluno, aluno - professor, aluno - aluno), envolvendo discussões, diálogos em grupo e maior interação com os colegas, professores e tutores.",
                "A aprendizagem acontece através apenas da interação entre (professor - aluno), com informações repassadas por um professor ou tutor.",
                "Não sei informar."
            ]
        },
        {
            'pergunta': "AVALIAÇÃO E ACOMPANHAMENTO CONTÍNUO",
            'opcoes': [
                "As avaliações não estão alinhadas com os objetivos educacionais propostos no planejamento do ensino.",
                "As avaliações são contínuas e alinhadas aos objetivos educacionais planejados. Elas são aplicadas com o propósito de monitorar o progresso do aprendizado (verificar se os objetivos foram alcançados), prover feedback para o aluno, daquilo que ele aprendeu e do que precisa aprender, identificando as falhas da aprendizagem e os aspectos da instrução que precisam ser modificados.",
                "Os objetivos educacionais não foram claramente definidos e as avaliações são aplicadas com um único propósito: atribuição de uma nota/conceito como forma de “classificar” o conhecimento do aluno como aprovado ou reprovado.",
                "Não sei informar."
            ]
        }
    ]
    total_questoes = len(questoes)

    if questao_num > total_questoes:
        return redirect('resultado_teste')

    if request.method == 'POST':
        resposta = request.POST.get('resposta')

        questao = questoes[questao_num - 1]
        texto = questao['pergunta']
        ordem = questao_num
        curso = request.user.aluno.curso  # Obtém o curso do aluno

        Resposta.objects.update_or_create(
            aluno=request.user.aluno,  # Referência correta ao Aluno
            questao_num=questao_num,
            defaults={
                'resposta': resposta,
                'texto': texto,
                'ordem': ordem,
                'curso': curso,  # Inclui o campo curso
            }
        )

        if questao_num < total_questoes:
            return redirect('teste_pbl_questao', questao_num=questao_num + 1)
        else:
            return redirect('resultado_teste')

    questao = questoes[questao_num - 1]

    try:
        resposta_usuario = Resposta.objects.get(
            aluno=request.user.aluno, questao_num=questao_num)
        resposta_selecionada = resposta_usuario.resposta
    except Resposta.DoesNotExist:
        resposta_selecionada = None

    context = {
        'questao': questao,
        'questao_num': questao_num,
        'total_questoes': total_questoes,
        'resposta_selecionada': resposta_selecionada
    }
    return render(request, 'cadastro_app/teste_pbl_questao.html', context)

@login_required
def resultado_teste(request):
    respostas_usuario = Resposta.objects.filter(
        aluno=request.user.aluno).order_by('questao_num')

    if not respostas_usuario.exists():
        return redirect('teste_pbl_questao', questao_num=1)

    respostas = [resp.resposta for resp in respostas_usuario]

    contagem_opcoes = {}
    for resposta in respostas:
        if resposta in contagem_opcoes:
            contagem_opcoes[resposta] += 1
        else:
            contagem_opcoes[resposta] = 1

    context = {
        'respostas': respostas_usuario,
        'contagem_opcoes': contagem_opcoes,
    }

    return render(request, 'cadastro_app/resultado_teste.html', context)

def escolha_perfil(request):
    return render(request, 'cadastro_app/aluno_professor.html')

# Adicionando as Views de Login

User = get_user_model()

def login_aluno(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    # Verifica se o usuário é um aluno
                    if hasattr(user, 'aluno'):
                        login(request, user)
                        return redirect('home')  # Redireciona para a tela 'home' após o login do aluno
                    else:
                        messages.error(request, 'Você não está cadastrado como Aluno.')
                except Aluno.DoesNotExist:
                    messages.error(request, 'Você não está cadastrado como Aluno.')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Informações inválidas. Verifique e tente novamente.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'cadastro_app/login_aluno.html', {'form': form})

def login_professor(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    # Verifica se o usuário é um professor
                    if hasattr(user, 'professor'):
                        login(request, user)
                        return redirect('inicio_professor')  # Redireciona para a tela de professor
                    else:
                        messages.error(request, 'Você não está cadastrado como Professor.')
                except Professor.DoesNotExist:
                    messages.error(request, 'Você não está cadastrado como Professor.')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Informações inválidas. Verifique e tente novamente.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'cadastro_app/login_professor.html', {'form': form})
