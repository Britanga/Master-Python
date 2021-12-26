"""
Variables locales: Se definen dentro de la función y no
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función
y estan disponible dentro y fuera de ellas.
"""

# Variable global

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def HolaMundo():
    frase = "Hola mundo!!"  # Variable local
    print("Dentro de la función:")
    print(frase)

    year = 2021             # Variable local
    print(year)

    global website          # Convertir a variable global
    website = "jesusbritoweb.es"
    print("Dentro: ", website)

    return "dato devuelto" + " " + str(year) # Para acceder a year es necesario el return


print(HolaMundo())          # Llamando a función
print("Fuera: ", website)   # Llamando a variable global