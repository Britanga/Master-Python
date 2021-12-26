"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""

# While
coleccion = []
x = 0

while x < 120:
    coleccion.append(f"Elemento-{x}")           # Añade a la lista
    print("Mostrando el: " + coleccion[x])
    x += 1

print(coleccion)        # Muestra toda la lista
print(coleccion[77])    # Muestra 1 elemento en específico de la lista


"""
# For
coleccion = []

for contador in range(0,120):
    coleccion.append(f"Elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)
"""