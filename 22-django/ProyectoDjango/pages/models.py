from django.db import models
from ckeditor.fields import RichTextField # Para usar RichTextField

# Create your models here.
"""
Modelo: Es la parte que se conecta/interactua con la BaseDatos.
(Los modelos son las entidades/tablas de la BaseDatos)
"""

# Crea modelo (Model indica que es un modelo)
# Nombres en singular es más recomendable, pero usar plural también se puede

class Page(models.Model):
    # verbose_name para cambiar nombre de las propiedades
    title = models.CharField(max_length=50, verbose_name="Título") # CharField = Varchar o string en Python
    #content= models.TextField(verbose_name="Contenido") # TextField = Campo de texto
    # Content en lugar de TextField será ahora RichTextField (Editor de texto enriquecido)
    content= RichTextField(verbose_name="Contenido")
    # slug Para hacer una url amigable (unique = no se repita el mismo URL)
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    # Nuevo atributo antes de "visible"
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(verbose_name="¿Visible?") # Si es publico o no
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el") # Fecha de creación (1sola vez)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el") # Fecha de actualización/editado

    class Meta: # Cambiar nombres y ordenacion
        verbose_name = "Página"           # Cambia nombre a singular
        verbose_name_plural = "Páginas"   # Cambia nombre a plural

    # Método mágico cambia nombre de las paginas a string"titulo+(publicado/privado)"
    def __str__(self):

        # Devuelve nombre de la pagina
        return self.title