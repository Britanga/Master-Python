from django.shortcuts import render
from .models import Page    # Para usar modelo "Page"
from django.contrib.auth.decorators import login_required # Bloquea paginas a no ser que este logueado

# Create your views here.

# Vistas de la app pages

# Decorador Bloquea paginas a no ser que este logueado
@login_required(login_url="login")
# Slug= Parámetro obligatorio
def page(request, slug):

    # Declaramos consulta SQL
    # Condicional (slug de la BD sea = al slug de la URL)
    page = Page.objects.get(slug=slug)

    # Pasar datos desde la vista y mostrarlos en la plantilla
    return render(request, 'pages/page.html', {
        #'title': 'Página individual',
        #'title': page.title, # No hace falta, se muestra en "page.html" directamente
        #'page': 'Hola Mundo desde la app Pages'
        'page': page
    })