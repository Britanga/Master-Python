from django.contrib import admin
from .models import Category, Article # Para usar los modelos

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    # Seleccionar columnas que estarán visibles en PanelAdministracion
    list_display = ('name', 'created_at')

    # Buscador
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin): # Muestra usuario, fechas de creación y actualización
    # Los parámetros son de solo lectura
    readonly_fields = ('user', 'created_at', 'update_at')

    # Buscador ("__" accede a todos los atributos de la tabla nombrada)
    search_fields = ('title', 'content', 'user__username', 'categories__name')

    # Seleccionar columnas que estarán visibles en PanelAdministracion
    list_display = ('title', 'user', 'public', 'created_at')

    # Filtro (coma necesaria para que interprete que es una tupla)
    list_filter = ('public', 'user__username', 'categories__name', )

    # Dentro del admin puedo personalizar ciertas cosas...
    # Ejm. Guardar automaticamente el usuario del PanelAdministración
    def save_model(self, request, obj, form, change):
        if not obj.user_id: # Sino llega un user...
            obj.user_id = request.user.id # AsignaObjeto del usuario identificado
        # Guarda Objeto
        obj.save()

# Register your models here.

# Cargar modelos
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)