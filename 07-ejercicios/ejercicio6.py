"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el título de la tabla y luego las multiplicaciones del 1 al 10.
"""

for cabecera in range (1,11):
    print("################################")
    print(f"######### TABLA DEL {cabecera} #########")
    print("################################")

    for numero in range (1,11):
        print(f"{cabecera} x {numero} = {cabecera*numero}")

    print("\n")