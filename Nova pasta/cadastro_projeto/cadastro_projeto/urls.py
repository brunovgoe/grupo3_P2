# cadastro_projeto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro_app.urls')),  # Inclui as URLs do cadastro_app
]
