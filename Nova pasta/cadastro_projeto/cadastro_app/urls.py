# cadastro_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.escolha_perfil, name='pagina_inicial'),  # Página inicial (Escolha de Perfil)
    path('home/', views.home, name='home'),  # Página inicial do aluno após login
    path('inicio_professor/', views.inicio_professor, name='inicio_professor'),  # Página inicial do professor
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_professor/', views.cadastrar_professor, name='cadastrar_professor'),
    path('login_aluno/', views.login_aluno, name='login_aluno'),
    path('login_professor/', views.login_professor, name='login_professor'),
    path('resumo_pbl/', views.resumo_pbl, name='resumo_pbl'),
    path('confirmar_leitura/', views.confirmar_leitura, name='confirmar_leitura'),
    path('teste_pbl/', views.teste_pbl, name='teste_pbl'),
    path('teste_pbl/questao/<int:questao_num>/', views.teste_pbl_questao, name='teste_pbl_questao'),
    path('resultado_teste/', views.resultado_teste, name='resultado_teste'),
]
