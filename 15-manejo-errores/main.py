# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores

"""
try:        # Intenta ejecutar las instrucciones
    nombre = input("¿Cuál es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:     # Si IF no se cumple
    print("Ha ocurrido un error, mete bien el nombre")
else:       # Si IF se cumple
    print("Todo ha funcionado correctamente")
finally:    # Al finalizar, muestra msj.
    print("Fin de la iteración !!")
"""

# Multiples excepciones
"""
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo!!")
#except ValueError:
#    print("Introduce un número correcto !!")
except Exception as e:
    print(type(e))  # Puedo acceder al tipo de dato del objeto si fuera necesario
    print("Ha ocurrido un error: ", type(e).__name__)   # Muestra el nombre del error
"""

# Excepciones personalizadas o lanzar excepcion

try:                    # Para limpiar las líneas de error
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real") # También TypeError u otro tipo de error
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre} !!")
except ValueError:      # Y que muestre este msj.
    print("Introduce los datos correctamente !!")
except Exception as e:  # Muestra el nombre del error, si comentaramos el ValueError de arriba
    print("Existe un error ", e)