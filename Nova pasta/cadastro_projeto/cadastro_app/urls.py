# cadastro_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.escolha_perfil, name='pagina_inicial'),
    path('home/', views.home, name='home'),
    path('pagina_inicial_professor/', views.inicio_professor,name='pagina_inicial_professor'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_professor/', views.cadastrar_professor,name='cadastrar_professor'),
    path('login_aluno/', views.login_aluno, name='login_aluno'),
    path('login_professor/', views.login_professor, name='login_professor'),
    path('resumo_pbl/', views.resumo_pbl, name='resumo_pbl'),
    path('confirmar_leitura/', views.confirmar_leitura, name='confirmar_leitura'),
    path('teste_pbl/', views.teste_pbl, name='teste_pbl'),
    path('teste_pbl/questao/<int:questao_num>/',views.teste_pbl_questao, name='teste_pbl_questao'),
    path('resultado_teste/', views.resultado_teste, name='resultado_teste'),
    path('resultados_por_curso/', views.resultados_por_curso,name='resultados_por_curso'),
    path('resultados_por_pergunta/', views.resultados_por_pergunta,name='resultados_por_pergunta'),
]
