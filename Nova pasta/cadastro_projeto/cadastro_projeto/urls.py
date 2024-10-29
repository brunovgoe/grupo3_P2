# projeto_principal/urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro_app.urls')),  # Inclui as URLs do cadastro_app
    path('', RedirectView.as_view(url='/cadastro/aluno/', permanent=False)),  # Redireciona a raiz para /cadastro/aluno/
]
