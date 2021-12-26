from django.contrib import admin # Predeterminado (Permite configurar el panel de admin)
from .models import Page # Para usar los modelos

# Configuración del listado
class PageAdmin(admin.ModelAdmin):

    # Campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')

    # Buscador
    search_fields = ('title', 'content')

    # Filtro (coma necesaria para que interprete que es una tupla)
    list_filter = ('visible',)

    # Seleccionar columnas que estarán visibles en PanelAdministracion
    list_display = ('title', 'visible', 'created_at')

    # Ordenación por defecto
    ordering = ('-created_at',) # con - ordena de forma inversa
    #ordering = ('created_at',)

# Register your models here.

# Cargar modelos dentro del panel de administracion
# (Muestra Título|Contenido|URL|Orden|Visible, MuestraFechas)
admin.site.register(Page, PageAdmin)

# Configurar el titulo del panel y parte 2 de la cabecera
title = "Proyecto con Django" # Para usarlo varias veces
subtitle = "Panel de gestión"
admin.site.site_header = title

# Parte 1 de la cabecera del panel
admin.site.site_title = title

# Configurar el subtitulo del panel
admin.site.index_title = subtitle