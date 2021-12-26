from django.shortcuts import render, get_object_or_404 # Mostrar error 404
from blog.models import Category, Article # Para usar modelos
from django.core.paginator import Paginator # Permite hacer la paginación
from django.contrib.auth.decorators import login_required # Bloquea paginas a no ser que este logueado

# Create your views here.

# Decorador Bloquea paginas a no ser que este logueado
@login_required(login_url="login")
# Crear vista nueva
def list(request):

    # Variable selecciona todos los objetos del modelo "Article"
    articles = Article.objects.all()

    # Variable de paginación (modelo, n° articulos por pagina)
    paginator = Paginator(articles, 3)

    # Recoger numero pagina
    page = request.GET.get('page')
    # Guarda todos los articulos de la pagina paginados
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        #'articles': articles
        'articles': page_articles
    })

@login_required(login_url="login")
# Vista para cada categoria
def category(request, category_id):

    # Usando error 404
    category = get_object_or_404(Category, id=category_id)
    # Variable selecciona todos los objetos del modelo "Article" cuya categoria = category
    #articles = Article.objects.filter(categories=category)

    return render(request, 'categories/category.html',{
        'category': category,
        #'articles': articles # Muestra articulos relacionados con la misma categoria
    })

@login_required(login_url="login")
def article(request, article_id):

    # Usando error 404
    article = get_object_or_404(Article, id=article_id)
    # Variable selecciona todos los objetos del modelo "Article" cuyo articulo = article

    return render(request, 'articles/detail.html',{
        'article': article
    })