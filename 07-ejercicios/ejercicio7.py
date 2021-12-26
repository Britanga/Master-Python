"""
Ejercicio 7. Hacer un  programa que muestre todos los números impares
entre dos números que decida el usuario.
"""

numero1 = int(input("Digite primer número: "))
numero2 = int(input("Digite segundo número: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2+1)):
        if contador%2 != 0:
            print(contador)

else:
    print("El primer número debe ser menor al segundo")