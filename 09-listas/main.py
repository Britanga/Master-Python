"""
Listas (arrays)
Son colecciones o conjunto de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice númerico.
"""

pelicula = "Batman"

#Definir listas
peliculas = ["Batman", "Spiderman", "El señor de los anillos"] # Ejm: Índice 0 es Batman
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))   # Tupla convertida en lista
years = list(range(2020, 2050)) # El rango devuelve los valores que necesita la lista
variada = ["Jesús", 30, 4.4, True, "Texto"] # Siguen siendo el tipo de dato correspondiente

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)"""

# Índices
pelicula = "Otra cosa"          # Modificando variable
peliculas[1] = "Gran Torino"    # Modificando índices
peliculas[2] = "El hobbit"
print(peliculas)

print(peliculas[1])     # De izq. a der. empieza en 0
print(peliculas[-2])    # De der. a izq. empieza en -1
print(cantantes[1:3])   # Accede al índice 1 y 2, la der. del rango no cuenta
print(peliculas[1:])    # Accede a todos los índices apartir del 1

# Añadir elementos a lista
cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)
"""
# Agregando elementos al listado para mostrarlos
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":   # If para no agregar "parar" dentro del listado
        peliculas.append(nueva_pelicula)

# Recorrer lista
print("\n********* LISTADO PELÍCULAS *********")

for pelicula in peliculas:  # Mientras que haya elementos en peliculas seguirá iterando
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
    # Index: Indica el n° del índice de "pelicula" dentro de la lista "peliculas"
    # pelicula es una variable local, como si fuera "contador"
"""
# Listas multidimensionales
print("\n********** Listado de contactos **********")
contactos = [
    [
        'Jesús',
        'jesus@gmail.com'
    ],
    [
        'Luis',
        'luis@gmail.com'
    ],
    [
        'Adrianis',
        'adrianis@gmail.com'
    ]
]

for contacto in contactos:      # contactos será 0, 1 y 2
    for elemento in contacto:   # y elemento será el n° de la der. como el print de abajo
        if contacto.index(elemento) == 0:   # Index: Indica el n° del índice de 
            print("Nombre: " + elemento)    # "elemento" dentro de la lista "contacto"
        else:
            print("Email: " + elemento)
    print("\n")      

# print(contactos[1][1]) # Accediendo a 1 elemento en concreto de la lista multidimensional