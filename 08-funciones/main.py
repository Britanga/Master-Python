"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametro):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1. Muestra el bloque de instrucciones de la función
print("##### EJEMPLO 1 #####")

# Definir función
def muestraNombre():
    print("Jesús")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

# Invocar función
muestraNombre()
muestraNombre()
muestraNombre()
"""
# Ejemplo 2. Introduce 2 parámetros y ejecuta la función
print("##### EJEMPLO 2 #####")

def muestraTuNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tú nombre: ")
edad = int(input("Introduce tu edad: "))
muestraTuNombre(nombre, edad)"""

# Ejemplo 3. Muestra tabla de multiplicar de parámetros asignados
print("##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range (11):
        print(f"{numero} x {contador} = {numero*contador}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1 Muestra tabla de multiplicar del 1 al 10
print("---------------------------------")

for numero_tabla in range (1,11):
    tabla(numero_tabla)

# Ejemplo 4. Parámetros opcionales
print("##### EJEMPLO 4 #####")

def getEmpleado(nombre, dni = None): # dni puede ser False o True también
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Jesús Brito", 4532415664)

# Ejemplo 5. Return o devolver datos
print("\n##### EJEMPLO 5 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo # Estoy devolviendo, mas no imprimiendo

print(saludame("Jesús Brito"))

# Ejemplo 6. Calculadora con parámetro opcional
print("\n##### EJEMPLO 6 #####")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:    # Mostrará suma y resta
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:                   # Sino, mostrará multiplicación y división
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(56, 5, True))

# Ejemplo 7. Función dentro de otra
print("\n##### EJEMPLO 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def getDevuelveTodo(nombre, apellidos): # Invocamos 1era y 2da función
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(getDevuelveTodo("Jesús", "Brito Molina"))

# Ejemplo 8. Función lambda. Es una función anónima que sirven para tareas simples.
print("\n##### EJEMPLO 8 #####")

dime_el_year = lambda year: f"El año es {year * 50}" # Todo esta en 1 sola linea

print(dime_el_year(2034))