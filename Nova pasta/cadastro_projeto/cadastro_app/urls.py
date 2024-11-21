from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rota para a página inicial
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('home/', views.home, name='home'),

    # Rotas relacionadas ao PBL
    path('resumo_pbl/', views.resumo_pbl, name='resumo_pbl'),
    path('confirmar_leitura/', views.confirmar_leitura, name='confirmar_leitura'),
    
    # Rotas de cadastro e login de aluno
    path('cadastro/aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('login/aluno/', auth_views.LoginView.as_view(
        template_name='cadastro_app/login_aluno.html',
        redirect_authenticated_user=True,
        next_page='home'  # Adicionado conforme sugestão
    ), name='login_aluno'),

    # Rotas de cadastro e login de professor
    path('cadastro/professor/', views.cadastrar_professor, name='cadastrar_professor'),
    path('login/professor/', auth_views.LoginView.as_view(
        template_name='cadastro_app/login_professor.html',
        next_page='home'
    ), name='login_professor'),

    # Rotas de cadastro e login de instituição
    path('cadastro/instituicao/', views.cadastrar_instituicao, name='cadastrar_instituicao'),
    path('login/instituicao/', auth_views.LoginView.as_view(
        template_name='cadastro_app/login_instituicao.html',
        next_page='home'
    ), name='login_instituicao'),

    # Rota de logout, aplicável a qualquer tipo de usuário
    path('logout/', auth_views.LogoutView.as_view(
        template_name='cadastro_app/logout.html'
    ), name='logout'),
    
    path('teste_pbl/questao/<int:questao_num>/', views.teste_pbl_questao, name='teste_pbl_questao'),
    
    path('resultado_teste/', views.resultado_teste, name='resultado_teste'),
    path('escolha_perfil/', views.escolha_perfil, name='escolha_perfil'),
]
