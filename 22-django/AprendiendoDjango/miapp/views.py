from django.shortcuts import render, HttpResponse, redirect
# HttpResponse = texto / redirect = redirecciones
from miapp.models import Article # Para usar modelos
from django.db.models import Q # Para usar OR en consultas
from miapp.forms import FormArticle # Para usar la clase formulario
from django.contrib import messages # Para usar msj flash

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)
# MVT = MVC, la Vista es Template y Controlador es Vista

# Menú con hipervínculos
layout = """
<h1>Sitio web con Django | Jesús Brito</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a>
    </li>
</ul>
<hr/>
"""

# Estamos en MVT usando 3 Vistas
def index(request): # Inicio

    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    ""

    # Demostrando que se puede usar while y if en django
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"
    """

    # Ciclo for en la plantilla
    year = 2021
    hasta = range(year, 2051)

    # Recomendable siempre crear las variables en la vista y no en los templates
    nombre = 'Jesús Brito'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    #return HttpResponse(layout+html)
    #return render(request, 'index.html')

    # Pasar datos desde la vista y mostrarlos en la plantilla
    return render(request, 'index.html', {
        'title': 'Inicio 2',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):# es un párametro que permite recibir datos de peticiones a esta url
    #return HttpResponse(layout+"""
    #    <h1>Hola mundo con Django!!</h1>
    #    <h3>Soy Jesús Brito WEB</h3>
    #""")
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0): # pagina de pruebas

    if redirigir == 1:
        #return redirect('/inicio/') # Redirecciona
        #return redirect('/contacto/Jesús/Brito/')
        return redirect('contacto', nombre="Jesús", apellidos="Brito")
        # Ventaja: Al usar "name" de urlpatterns, redirecciona a pesar de cambiar la url
        # (En este caso la cambiamos de contacto/ a contacto-dos/)

    #return HttpResponse(layout+"""
    #    <h1>Página de mi web</h1>
    #    <p>Creado por Jesús Brito</p>
    #""")
    #return render(request, 'pagina.html')

    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellidos=""):
    html = ""
    
    if nombre and apellidos: # Parámetro opcional
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):

    # Crear modelo Article
    """
    articulo = Article(
        title = 'Primer articulo!!',
        content = 'Contenido del articulo',
        public = True
    )"""

    # Crear modelo Article usando parámetros de la url (propiedadClase / parámetroURL)
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    # Guardar datos en la BD usando modelo
    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request): # Devuelve msj

    # Comprobar si nos llegan datos por GET
    #if request.method == 'GET':
    # Comprobar si nos llegan datos por POST
    # (Es más seguro xq no muestra el guardado en el url)
    if request.method == 'POST':

        # Crear variables para recibir datos
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        # Validar titulo
        if len(title) <= 5:
            return HttpResponse("El titulo es muy pequeño")

        # Crear modelo Article usando parámetros de la url (propiedadClase / parámetroURL)
        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        # Guardar datos en la BD usando modelo
        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

def create_article(request): # Devuelve a pagina

    return render(request, 'create_article.html')

def create_full_article(request): # Redirecciona a pagina 'articulos', sino devuelve formulario vacio

    # Comprobar si nos llegan datos por POST
    # (Es más seguro xq no muestra el guardado en el url)
    if request.method == 'POST':
        # request.POST limpia y valida para acceder de mejor manera a los datos
        formulario = FormArticle(request.POST)
        if formulario.is_valid(): # Si formulario es valido
            data_form = formulario.cleaned_data # Llegan los datos limpios

            # Recoger datos
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            # Crear modelo Article usando parámetros de la url (propiedadClase / parámetroURL)
            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            # Guardar datos en la BD usando modelo
            articulo.save()

            # Crear mensaje flash (Sesión que solo se muestra una vez)
            # Msj de guardado correcto
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            # Redireccion a otra pagina
            return redirect('articulos')

            # Devuelve datos
            #return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))

    else:
        # Crea objeto de la clase "FormArticle"
        formulario = FormArticle() # Genera formulario vacio

    return render(request, 'create_full_article.html', {
        'form': formulario
    })

def articulo(request): # Sacar datos y elementos de la base de datos

    # Accede/saca objeto del modelo
    try:
        #articulo = Article.objects.get(id=8)
        #articulo = Article.objects.get(pk=8)
        articulo = Article.objects.get(title="Superman", public=False) # Cumplirse los 2 parámetros
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado<h1/>"

    return HttpResponse(response)

def editar_articulo(request, id):

    # Selecciona articulo con el id escogido por el usuario
    articulo = Article.objects.get(pk=id)

    # Actualiza registro
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    # Guarda edición del registro
    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):

    # Selecciona todos los articulos
    #articulos = Article.objects.all()

    # Ordena por orden númerico
    #articulos = Article.objects.order_by('id')

    # Ordena todos los articulos publicados por orden númerico inverso
    articulos = Article.objects.filter(public=True).order_by('-id')

    # Ordena por orden alfabetico
    #articulos = Article.objects.order_by('title')

    # Ordena por orden alfabetico inverso
    #articulos = Article.objects.order_by('-title')

    # Limite de x elementos
    #articulos = Article.objects.order_by('id')[:3]

    # Limite de x hasta x elementos
    #articulos = Article.objects.order_by('id')[3:8]

    # Consultas con condiciones, filter y lookups

    # Que cumpla 2 condiciones
    #articulos = Article.objects.filter(title="Batman", id=8)
    # Que contenga elemento
    #articulos = Article.objects.filter(title__contains="articulo")
    # Que elemento sea exacto (incluyendo mayusculas y minusculas)
    #articulos = Article.objects.filter(title__exact="articulo")
    # Que elemento sea exacto (excluyendo mayusculas y minusculas)
    #articulos = Article.objects.filter(title__iexact="articulo")
    # Que id sea mayor a... con greater than (__gt)
    #articulos = Article.objects.filter(id__gt=11)
    # Que id sea mayor o igual a... con greater than (__gte)
    #articulos = Article.objects.filter(id__gte=11)
    # Que id sea menor a... con lest than (__lt)
    #articulos = Article.objects.filter(id__lt=12)
    # Que id sea menor o igual a... con lest than (__lte)
    #articulos = Article.objects.filter(id__lte=12)
    # Que id sea menor o igual a... y contenga elemento
    #articulos = Article.objects.filter(id__lte=12, title__contains="2")

    # Consultas con exclude
    """
    articulos = Article.objects.filter(
                                    title="Articulo",
                                    public=True
                                ) # Tabulacion solo para demostrar q puede ser como uno quiera
                                """
    """
    articulos = Article.objects.filter(
                                    title="Articulo"
                                ).exclude(
                                    public=False
                                )"""

    # Consultas con OR
    # Que contenga elemento "2" o sea "publico"
    """
    articulos = Article.objects.filter(
        Q(title__contains="2") | Q(public=True)
    )"""

    # Consultas con SQL (Sirve por si no sabe hacer consultas con django como arriba)

    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 2' AND public=0")

    """Nota: Se puede seleccionar un atributo de la tabla (junto con id q es obligatorio)
    Ejm. SELECT id, title para sacar solo titulo
    (es necesario borrar los demas atributos que no estan en el select en articulos.html)

    Recomendable usar las consultas de arriba que son con Django xq si llegas a cambiar
    de base de datos la consulta siempre sera igual (Django se encarga de ejecutar el SQL)
    """

    #return HttpResponse(articulos) # Comprueba que existe un listado de articulos
    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):

    # Selecciona articulo con el id escogido por el usuario
    articulo = Article.objects.get(pk=id)
    # Elimina registro del articulo
    articulo.delete()

    return redirect('articulos') # parámetro "name" del fichero "urls.py"