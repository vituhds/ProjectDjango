from django.contrib import admin

# Register your models here.

from siteHome.models import PaginaInicial


@admin.register(PaginaInicial)
class PaginaInicialsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subTitulo', 'Criados', 'Modificado', 'Ativo')

