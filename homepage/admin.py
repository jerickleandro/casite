from django.contrib import admin

# Register your models here.
from .models import Categoria, Noticia

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('category', 'ativo', 'modificados')

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'category', 'ativo', 'modificados')


 