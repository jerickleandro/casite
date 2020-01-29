from django.contrib import admin

# Register your models here.
from .models import Categoria, Noticia, Membros, Labs

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('category', 'ativo', 'modificados')

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'category', 'ativo', 'modificados')

@admin.register(Membros)
class MembrosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificados')

@admin.register(Labs)
class LabsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificados')
 