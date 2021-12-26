"""
# Condicional IF

Si se cumple esta condición:
    Ejecutar grupo de instrucciones
Si no:
    Ejecutar otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


Operadores de comparación:
==  igual
!=  diferente
<   menor que
>   mayor que
<=  menor o igual que
>=  mayor o igual que

Operadores lógicos:
and Y
or  O
!   Negación
not NO

"""

# Ejemplo 1:
print("################# EJEMPLO 1 #################")

color = "verde"
#color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es Rojo")
else:
    print("Color incorrecto")


# Ejemplo 2:
print("\n################# EJEMPLO 2 #################")

year = 2020
# year = int(input("¿En qué año estamos?: "))

if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")

# Ejemplo 3:
print("\n################# EJEMPLO 3 #################")

nombre = "Jesús Brito"
ciudad = "Barcelona"
continente = "Europa"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    
    if(continente != "Europa"): # Manera correcta: Xq comprobamos una variable diferente
        print("El usuario NO es europeo")
    else:
        print(f"Es europeo y de ciudad {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4:
print("\n################# EJEMPLO 4 #################")

# dia = int(input("Introduce el número del día de la semana: "))
dia = 2

""" Manera innecesaria
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""
# Manera correcta: Xq comprobamos una misma variable
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Ejemplo 5:
print("\n################# EJEMPLO 5 #################")

edad_minima = 18
edad_maxima = 65
# edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No esta en edad de trabajar")

# Ejemplo 6:
print("\n################# EJEMPLO 6 #################")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} Es un país de habla hispana !!")
else:
    print(f"{pais} NO es un país de habla hispana :(")

# Ejemplo 7:
print("\n################# EJEMPLO 7 #################")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SI es un país de habla hispana :)")

# Ejemplo 8:
print("\n################# EJEMPLO 8 #################")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SI es un país de habla hispana :)")