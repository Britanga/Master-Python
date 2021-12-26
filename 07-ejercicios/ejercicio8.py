"""
Ejercicio 8. ¿Cuánto es el X porciento de X número?
                         20% de 150
"""

numero = int(input("Introduce número: "))
porcentaje = int(input(f"¿Cuánto porcentaje desea retirar de {numero}?: "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")