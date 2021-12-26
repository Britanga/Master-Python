from django.urls import path # Para usar las rutas con path
from . import views # Para usar Vistas de la app pages (from . indica directorio actual)

urlpatterns = [
    # URL vinculadas con la app blog
    path('articulos/', views.list, name="list_articles"),
    path('categoria/<int:category_id>', views.category, name="category"),
    path('articulo/<int:article_id>', views.article, name="article")
]