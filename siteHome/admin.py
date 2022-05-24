from django.contrib import admin

# Register your models here.

from siteHome.models import PaginaInicial


@admin.register(PaginaInicial)
class PaginaInicialsAdmin(admin.ModelAdmin):
    list_display = ('Titulo_Header', 'SubTitulo_Header', 'Criados', 'Modificado', 'Ativo')

