
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

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