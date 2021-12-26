"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.

La importancia es que a diferencia de una lista que sus índices son númericos
los diccionarios sus índices son textos, lo cual hace más facil de recordar
ya que son índices asociativos y funciona mejor cuando son muchos datos que guardar y mostrar.
"""

persona = {
    "nombre": "Jesús",
    "apellidos": "Brito",
    "web": "jesusbritoweb.es"
}

print(type(persona))
print(persona)
print(persona["apellidos"]) # Acceder a un valor del diccionario
print(persona["web"])       # Igual

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@gmail.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@gmail.com'
    }
]

print(contactos)
contactos[0]['nombre'] = "Antoñito" # Sustituye un valor del diccionario de la lista
print(contactos[0]['nombre'])       # Muestra un valor del diccionario de la lista

print("\nListado de contactos: ")
print("-------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}") # Concatenación de texto con
    print(f"Email del contacto: {contacto['email']}")   # Valor del diccionario
    print("-------------------------------")