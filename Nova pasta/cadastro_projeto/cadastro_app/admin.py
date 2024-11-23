# cadastro_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    UsuarioPersonalizado,
    Resposta,
    Professor,
    Aluno,
    Curso,
    QuestaoTeste,
)

class UsuarioPersonalizadoAdmin(UserAdmin):
    model = UsuarioPersonalizado
    # Removido 'tipo_usuario' pois não existe no modelo
    fieldsets = UserAdmin.fieldsets + (
        # (None, {'fields': ('tipo_usuario',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nome_completo', 'email')}),
    )
    list_display = ('username', 'email', 'nome_completo', 'is_staff')
    search_fields = ('email', 'nome_completo')
    ordering = ('email',)

@admin.register(Resposta)
class RespostaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'questao_num', 'resposta')
    list_filter = ('aluno', 'questao_num')
    search_fields = ('aluno__usuario__username', 'resposta')

# Registrar a classe customizada de UsuarioPersonalizado
admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)

# Registrar outros modelos
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(QuestaoTeste)
