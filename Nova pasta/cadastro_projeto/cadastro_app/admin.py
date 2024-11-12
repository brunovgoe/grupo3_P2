from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoAdmin(UserAdmin):
    model = UsuarioPersonalizado
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo_usuario',)}),
    )

admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)