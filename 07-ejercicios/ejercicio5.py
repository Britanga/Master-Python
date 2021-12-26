"""
Ejercicio 5. Hacer un programa que muestre todos los números entre
dos números que diga el usuario.
"""

numero1 = int(input("Digite primer número: "))
numero2 = int(input("Digite segundo número: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)): # contador se autoinicializa en numero1
        print(contador)                        # no hace falta añadir +1 en los ciclos for
else:
    print("El número 1 debe ser menor al número 2")