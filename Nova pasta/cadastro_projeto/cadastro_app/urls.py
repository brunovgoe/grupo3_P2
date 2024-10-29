from django.urls import path
from .views import cadastrar_aluno, cadastrar_professor, cadastrar_instituicao

urlpatterns = [
    path('aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('professor/', cadastrar_professor, name='cadastrar_professor'),
    path('instituicao/', cadastrar_instituicao, name='cadastrar_instituicao'),
]
