from django.db import models
from ckeditor.fields import RichTextField # Para usar RichTextField
from django.contrib.auth.models import User # Para relacionarlo con el modelo "Article"

# Create your models here.
"""
Modelo: Es la parte que se conecta/interactua con la BaseDatos.
(Los modelos son las entidades/tablas de la BaseDatos)
"""

# Crea modelo (Model indica que es un modelo)
# Nombres en singular es más recomendable, pero usar plural también se puede

class Category(models.Model):
    # verbose_name para cambiar nombre de las propiedades
    name = models.CharField(max_length=100, verbose_name="Nombre") # CharField = Varchar o string en Python
    description= models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el") # Fecha de creación (1sola vez)

    class Meta: # Cambiar nombres
        verbose_name = "Categoría"           # Cambia nombre a singular
        verbose_name_plural = "Categorías"   # Cambia nombre a plural

    # Método mágico cambia nombre de las paginas a string"titulo+(publicado/privado)"
    def __str__(self):

        # Devuelve nombre de la pagina
        return self.name

class Article(models.Model):
    # verbose_name para cambiar nombre de las propiedades
    title = models.CharField(max_length=150, verbose_name="Título") # CharField = Varchar o string en Python
    # Content en lugar de TextField será ahora RichTextField (Editor de texto enriquecido)
    content= RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles") # upload_to= carpetaGuardaImagenes
    public = models.BooleanField(verbose_name='Publicado?') # Si es publico o no
    # Guarda el ID del usuario que ha creado el articulo (relación de 1:1)
    # on_delete=models.CASCADE Si borro un usuario tambien se borraran todos sus articulos
    # editable=False No se verá cual es el usuario que creo el articulo
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    # Relación de 1:M muchos (1 articulo puede tener muchas categorías)
    # Crea una tabla relacionando una ID con otra ID
    categories = models.ManyToManyField(Category, verbose_name="Categorias", null=True, blank=True, related_name="articles") # Puede ser null o estar sin nada (blank)/ related_name= CambiaNombre
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el') # Fecha de creación (1sola vez)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado el') # Fecha de actualización/editado

    class Meta: # Cambiar nombres
        verbose_name = "Artículo"           # Cambia nombre a singular
        verbose_name_plural = "Artículos"   # Cambia nombre a plural

        # Cambiar criterio de ordenación
        ordering = ['-created_at'] # De más nuevo a más antiguo

    # Método mágico cambia nombre de las paginas a string"titulo+(publicado/privado)"
    def __str__(self):

        # Devuelve nombre de la pagina
        return self.title