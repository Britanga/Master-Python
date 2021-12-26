"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla *
- Hacer función que recorra listas de números y devuelva un string *
- Ordenarla y mostrarla *
- Mostrar su longitud *
- Buscar algún elemento (Que el usuario pida por teclado) *
"""

# Crear la lista
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

# Crear funcion que recorra lista y devuelva un string
def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado

# Recorrer y mostrar
print("###### Recorrer y mostrar ######")
"""
for numero in numeros:  # Se autoinicializa en el 1er parámetro de numeros
    print(numero)
"""
print(mostrarLista(numeros))
print(mostrarLista(numeros))
print(mostrarLista(["Victor", "Juan", "Pepe"])) # Sirve en dif. tipos de datos

# Ordenar y mostrar
print("###### Ordenar y mostrar ######")
numeros.sort()                                  # Ordena
print(mostrarLista(numeros))

# Mostrar longitud
print("###### Mostrar longitud ######")
print(len(numeros))                             # Cuenta

# Busqueda en la lista
try:    # Intenta ejecutar instrucciones
    print("###### Busqueda en la lista ######")

    busqueda = int(input("Introduce el número: "))

    comprobar = isinstance(busqueda, int)           # Comprueba si es entero

    while not comprobar or busqueda <= 0:           # Mientras no sea entero o n° negativo
        busqueda = int(input("Introduce el número: "))
    else:
        print(f"Haz introducido el {busqueda}")

    print(f"###### Buscar en la lista el número {busqueda} ######")

    search = numeros.index(busqueda)                # index guarda el índice
    print(f"El número buscado existe en la lista, es el índice: {search}")
except: # Si alguna instrucción no se cumple, suelta este msj.
    print("El número no esta en la lista, lo siento!!")