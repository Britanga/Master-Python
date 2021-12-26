"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un número multiplicado por si mismo) de los 60 primeros números
naturales. Resolverlo con for y while.
"""

"""
# WHILE

contador = 0               # es necesario declarar la variable contador en los ciclos while
while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1                               # no hace falta añadir +1 en los ciclos for
"""

# FOR

for numero in range(61):
    cuadrado = numero*numero
    print(f"El cuadrado de {numero} es {cuadrado}")