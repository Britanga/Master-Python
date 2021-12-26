from django.urls import path # Para usar las rutas con path
from . import views # Para usar Vistas de la app pages (from . indica directorio actual)

urlpatterns = [
    # URL vinculadas con la app principal
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    #path('sobre-nosotros/', views.about, name="about")
    path('registro/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]