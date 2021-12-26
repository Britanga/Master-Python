"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include para cargar las otras rutas
from django.conf import settings # Para usar MEDIA_URL

"""from mainapp import views # Usa vistas de la app principal"""
# Usa vistas de la app pages (as= NombreAlternativo xq views ya esta arriba)
#from pages import views as page_views
# Mejor manera de importarlo
"""import pages.views"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('pages.urls')),
    path('', include('blog.urls'))
]

# Ruta Imagenes (Para que funcione la subida de imagenes)
if settings.DEBUG: # Si el proyecto esta en modo DEBUG
    # Usar la forma de cargar ficheros estaticos del Framework para generar una URL basada en FicherosEstaticos
    from django.conf.urls.static import static

    # urlpatterns genera una nueva ruta estatica
    #(MEDIA_URL = '/media/' de settings.py, RutaAbsoluta donde esta el directorio de media)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
