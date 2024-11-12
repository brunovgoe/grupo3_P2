from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlunoForm, ProfessorForm, InstituicaoForm, UsuarioPersonalizadoCreationForm
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Aluno, Professor, Instituicao, Resposta


def pagina_inicial(request):
    return render(request, 'cadastro_app/inicio.html')


# View para a página inicial
@login_required
def home(request):
    resumo_lido = request.session.get('resumo_lido', False)
    return render(request, 'cadastro_app/home.html', {'resumo_lido': resumo_lido})


# View para cadastrar aluno
def cadastrar_aluno(request):
    if request.method == 'POST':
        usuario_form = UsuarioPersonalizadoCreationForm(request.POST)
        aluno_form = AlunoForm(request.POST)
        
        if usuario_form.is_valid() and aluno_form.is_valid():
            # Primeiro, salva o formulário do usuário personalizado
            usuario = usuario_form.save()

            # Cria o aluno associado ao usuário
            aluno = aluno_form.save(commit=False)
            aluno.usuario = usuario
            aluno.save()

            # Mensagem de sucesso e redirecionamento para a página de login
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('login_aluno')
        else:
            # Se houver erros no formulário, mostrar mensagens de erro
            messages.error(request, 'Houve um erro no cadastro. Verifique as informações.')
    else:
        usuario_form = UsuarioPersonalizadoCreationForm()
        aluno_form = AlunoForm()

    # Renderizar o template de cadastro com os dois formulários
    return render(request, 'cadastro_app/cadastrar_aluno.html', {
        'usuario_form': usuario_form,
        'aluno_form': aluno_form
    })

# View para cadastrar professor
def cadastrar_professor(request):
    if request.method == 'POST':
        usuario_form = UsuarioPersonalizadoCreationForm(request.POST)
        professor_form = ProfessorForm(request.POST)
        if usuario_form.is_valid() and professor_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.is_active = False  # Definir como inativo até a verificação, se necessário
            usuario.save()
            Professor.objects.create(usuario=usuario, departamento=professor_form.cleaned_data['departamento'])
            messages.success(request, 'Professor cadastrado com sucesso! Por favor, faça o login.')
            return redirect('login_professor')
    else:
        usuario_form = UsuarioPersonalizadoCreationForm()
        professor_form = ProfessorForm()
    return render(request, 'cadastro_app/cadastrar_professor.html', {'usuario_form': usuario_form, 'professor_form': professor_form})


# View para cadastrar instituição
def cadastrar_instituicao(request):
    if request.method == 'POST':
        usuario_form = UsuarioPersonalizadoCreationForm(request.POST)
        instituicao_form = InstituicaoForm(request.POST)
        if usuario_form.is_valid() and instituicao_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.is_active = False  # Definir como inativo até a verificação, se necessário
            usuario.save()
            Instituicao.objects.create(usuario=usuario, cnpj=instituicao_form.cleaned_data['cnpj'])
            messages.success(request, 'Instituição cadastrada com sucesso! Por favor, faça o login.')
            return redirect('login_instituicao')
    else:
        usuario_form = UsuarioPersonalizadoCreationForm()
        instituicao_form = InstituicaoForm()
    return render(request, 'cadastro_app/cadastrar_instituicao.html', {'usuario_form': usuario_form, 'instituicao_form': instituicao_form})


# View para a página de Resumo PBL
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

# View para cada questão do questionário
def teste_pbl_questao(request, questao_num):
    # Lista de questões para o questionário
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

    if questao_num > len(questoes):
        return redirect('home')  # Redireciona para a página inicial quando o questionário termina

    if request.method == 'POST':
        # Salvar a resposta do usuário
        resposta_texto = request.POST.get('resposta')
        Resposta.objects.create(
            texto=resposta_texto,
            ordem=questao_num
        )
        # Redireciona para a próxima pergunta
        return redirect('teste_pbl_questao', questao_num=questao_num + 1)

    # Renderiza a questão atual
    questao = questoes[questao_num - 1]
    context = {
        'questao': questao,
        'questao_num': questao_num,
        'proxima_questao': questao_num + 1
    }
    return render(request, 'cadastro_app/teste_pbl_questao.html', context)