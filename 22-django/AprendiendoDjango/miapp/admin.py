from django.contrib import admin # Predeterminado (Permite configurar el panel de admin)
from .models import Article, Category # Para usar los modelos

# Register your models here.

# Configuracion para q muestre la fecha
class ArticleAdmin(admin.ModelAdmin): # ModelAdmin= clase para manipular modelos en PanelAdmin
    # readonly_fields= indica q campos son de solo lectura para luego mostrarlos
    readonly_fields = ('created_at', 'update_at')


# Cargar modelos dentro del panel de administracion
admin.site.register(Article, ArticleAdmin) # ArticleAdmin= Muestra campos de solo lectura
admin.site.register(Category)

# Configurar el titulo del panel y parte 2 de la cabecera
title = "Master en Python - Jesús Brito 5" # Para usarlo varias veces
admin.site.site_header = title

# Parte 1 de la cabecera del panel
admin.site.site_title = title

# Configurar el subtitulo del panel
admin.site.index_title = "Panel de gestión"