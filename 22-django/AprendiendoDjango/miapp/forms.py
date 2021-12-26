from django import forms # Para usar formularios
from django.core import validators # Para validar diferentes tipos de datos

# Es mejor una clase con todas las funciones dentro, q las funciones x separado
# Contiene 3 atributos (title, content y public)
class FormArticle(forms.Form): # Parámetro para heredar funcion Form de clase forms

    # Crea variables
    title = forms.CharField(
        label = "Titulo",
        # Personalizar
        max_length=20, # 20 caracteres maximo
        required=True,  # Campo obligatorio
        widget=forms.TextInput( # Cambia formato
            attrs={ # atributos
                'placeholder': 'Mete el titulo',
                'class': 'titulo_form_article' # Crea clase
            }
        ),
        # Validaciones
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            # (ExpresiónRegular, Mensaje, CodigoError)
            # RegexValidator acepta solo letras mayusculas y minusculas, ñ, números y espacio
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(50, 'Te has pasado, has puesto mucho texto')
        ]
    )
    # Actualiza atributos del formato widget
    content.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'contenido_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )