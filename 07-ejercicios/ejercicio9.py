"""
Ejercicio 9. Hacer un programa que pida números al usuario
indefinidamente hasta meter el numero 111
"""
contador = 1
while contador < 100: # Ya que contador siempre será 1 esto, es un bucle infinito
    numero = int(input("Digite número: "))

    if numero == 111: # Hasta que introduzcan el 111
        break
    else:
        print(f"Haz introducido el: {numero}")