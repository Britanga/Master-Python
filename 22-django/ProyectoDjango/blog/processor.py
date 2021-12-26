from blog.models import Category, Article # Para usar modelo "Category" y "Article"

""" Context processors: Es una opcion que nos permite tener informacion en todas
nuestras templates
"""

def get_categories(request): # Devuelve menú con las categorias

    # Selecciona atributos de la BD (flat=True convierte en string)
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    
    # Selecciona atributos de la BD
    # Subconsultas en Django con filter(ID_Categorias = ID_CategoriasEnUso) de categorías que tienen articulos publicados
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    # Devuelve atributos de la BD
    return {
        'categories': categories,
        'ids': categories_in_use
    }