from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado, Resposta

class UsuarioPersonalizadoAdmin(UserAdmin):
    model = UsuarioPersonalizado
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo_usuario',)}),
    )

admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)

@admin.register(Resposta)
class RespostaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'questao_num', 'resposta')
    list_filter = ('usuario', 'questao_num')
    search_fields = ('usuario__username', 'resposta')