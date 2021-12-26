from django.urls import path # Para usar las rutas con path
from . import views # Para usar Vistas de la app pages (from . indica directorio actual)

urlpatterns = [
    # URL vinculadas con la app de paginas
    #path('pagina/<str:slug>', pages.views.page, name="page")
    path('pagina/<str:slug>', views.page, name="page")
]