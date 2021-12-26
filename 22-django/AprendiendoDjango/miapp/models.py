from django.db import models

# Create your models here.
"""
Modelo: Es la parte que se conecta/interactua con la BaseDatos.
(Los modelos son las entidades/tablas de la BaseDatos)
"""

# Crea modelo (Model indica que es un modelo)
# Nombres en singular es más recomendable, pero usar plural también se puede
class Article(models.Model):
    # verbose_name para cambiar nombre de las propiedades
    title = models.CharField(max_length=150, verbose_name="Título") # CharField = Varchar o string en Python
    content= models.TextField(verbose_name="Contenido") # TextField = Campo de texto
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to="articles") # upload_to= carpetaGuardaImagenes
    public = models.BooleanField(verbose_name="¿Publicado?") # Si es publico o no
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="creado") # Fecha de creación (1sola vez)
    update_at = models.DateTimeField(auto_now=True, verbose_name="editado") # Fecha de actualización/editado

    class Meta: # Cambiar nombres y ordenacion
        verbose_name = "Artículo"           # Cambia nombre a singular
        verbose_name_plural = "Artículos"   # Cambia nombre a plural
        #ordering = ['id']                   # Ordena de menor a mayor
        #ordering = ['-id']                   # de mayor a menor
        #ordering = ['public']               # de no publicados a publicados
        #ordering = ['-public']              # de publicados a no publicados
        #ordering = ['created_at']           # de más antiguo a más nuevo
        ordering = ['-created_at']           # de más nuevo a más antiguo

    # Método mágico cambia nombre de los articulos a string"titulo+(publicado/privado)"
    def __str__(self):

        # IF para usar "publicado" "privado" en lugar de 0 y 1 o False y True
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"

        return f"{self.title} {public}"
    

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField() # Fecha guardada manualmente

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

"""
Cada vez que se hace un cambio en las tablas, es necesario una migración
Migración: es el proceso de mover datos de una o más plataformas de origen
a otra base de datos de destino

- Crea migración
con el comando en cmd py manage.py makemigrations
(Se creo en el paquete "migrations"->0001_initial.py)

Declara la consulta en sqllite3
con el comando en cmd py manage.py sqlmigrate miapp 0001
(miapp = nombre de la app/ 0001 el número de la migración)

Ejecuta la consulta en sqllite3
con el comando en cmd py manage.py migrate

Nota: automáticamente en todas las tablas crea un ID autoincrementable

- Hacer cambios en la estructura de tablas y modelos
con el comando en cmd py manage.py makemigrations

Declara la consulta en sqllite3
con el comando en cmd py manage.py sqlmigrate miapp 0002
(miapp = nombre de la app/ 0002 el número de la migración)

Ejecuta la consulta en sqllite3
con el comando en cmd py manage.py migrate
"""