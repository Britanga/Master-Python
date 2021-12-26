"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/es/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y también podemos crear nuestros modulos
"""
# Importar modulo propio
# import mimodulo                       # Importa el modulo completo
# from mimodulo import holaMundo        # Importa una función dentro del modulo
from mimodulo import *                  # Importa el modulo completo

# print(mimodulo.holaMundo("Jesús Brito Web"))  # Muestra cada función
# print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Jesús Brito Web"))     # Muestra la función
print(calculadora(3, 5, True))

# Modulo fechas
import datetime
print(datetime.date.today())                # Fecha actual

fecha_completa = datetime.datetime.now()    # Fecha y Hora actual
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())  # Tiempo en formato Unix

# Modulo matemáticas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Número pi: ", float(math.pi))        # Podemos dejarlo en tipo de dato float

print("Redondear: ", math.ceil(6.56798))    # Redondea al alza

print("Redondear: ", math.floor(6.56798))   # Redondea a la baja

# Modulo ramdom
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15,67))