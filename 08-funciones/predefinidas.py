nombre = "Jesús Brito"

# Funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str) # Revisa si es string
if comprobar:   # Automáticamente entiende que se compara con un True
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):   # Revisa si no es flotante
    print("La variable no es un número con decimales")

# Limpiar espacios
frase = "  contenido  "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2021
print(year)
del year
# print(year) # Da error ya que se borro el contenido

# Comprobar variables vacías
texto = " ff  "

if len(texto) <= 0:     # len o length cuenta el n° elementos que tiene la variable
    print("La variable esta vacía")
else:
    print("La variable tiene contenido: ", len(texto))

# Encontrar carácteres
frase = "la vida es bella"
print(frase.find("vida"))   # Busca la palabra contando desde 0, en este caso es 3

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())