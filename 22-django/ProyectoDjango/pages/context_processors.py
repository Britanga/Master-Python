from pages.models import Page # Para usar modelo "Page"

""" Context processors: Es una opcion que nos permite tener informacion en todas
nuestras templates
"""

def get_pages(request): # Devuelve menú con las paginas
    
    # Selecciona atributos de la BD
    # (filter= Condicional solo si es True lo muestra)
    # (order_by= Ordena con la enumeración de "order")
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    # Saca un objeto completo de pagina y seria muy pesado
    #pages = Page.objects.all()
    # Si quisiera 1 solo atributo seria una tupla con 1 solo elemento
    #pages = Page.objects.values_list('title')
    # Si quiero que sea un string como tal seria con el flat
    #pages = Page.objects.values_list('title', flat=True)

    # Devuelve atributos de la BD
    return {
        'pages': pages
    }