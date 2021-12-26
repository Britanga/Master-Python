"""
Ejercicio 2. Escribir un script que nos muestre por pantalla
todos los números pares del 1 al 120.
"""

for contador in range(1,121): # contador se autoinicializa en 1
    if contador%2 == 0:
        print(contador)       # no hace falta añadir +1 en los ciclos for
    """
    else:
        print(f"{contador} es impar")
    """