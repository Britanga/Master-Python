from django.apps import AppConfig


class MiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miapp'
    # verbose_name para cambiar nombre de la app en el panel de administración
    # (No afecta la carpeta) funciona editando INSTALLED_APPS de "settings.py"
    verbose_name = 'Mi primera aplicación'