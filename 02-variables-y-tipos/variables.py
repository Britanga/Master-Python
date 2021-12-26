"""
Una variable es un contenedor de información
que dentro guardara datos, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""

# Crear variables y asignarle un valor
texto = "Máster en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

# Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("-------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("-------------------------------")

# Concatenación
nombre = "Jesús"
apellidos = "Brito"
web = "jesusbritoweb.es"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))

""" Aqui realmente nosotros no estamos aplicando una concatenación,
porque le estamos pasando unas variables como un parametro a la función print
para que ella se encargue de concatenar automáticamente con un espaciado de por medio
"""
print(nombre, apellidos, web)