from django import template # Para poder crear filtros

# Carga libreria de template
register = template.Library()

# Crear filtro
@register.filter(name='saludo')
def saludo(value):

    largo=''
    if len(value) >= 8:
        largo = '<p>Tú nombre es muy largo</p>'
    return f"<h1 style='background:green;color:white;'>Bienvenido, {value}</h1>"+largo

"""
Usamos condicionales y estilos para demostrar que se pueden usar en los filtros
(Se pueden crear filtros sin condicionales ni estilos)
"""