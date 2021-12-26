# - Tener las funciones definidas arriba del todo del fichero.

def mi_funcion(nombre): # - Los valores de las variables se pasen como parámetro 
    return "Hola que tal" + nombre

def mi_segunda_funcion(apellidos):  # a las funciones, y estas muestren los datos.
    return "Hola que tal 2" + apellidos # - En vez de hacer un print, devuelve un dato.

nombre = "Jesús"  # las variables tienen que estar definidas antes de invocar la función.
apellidos = "Brito"

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(mi_funcion(nombre))   # - Puedo acceder a variables globales dentro de las funciones
print(mi_segunda_funcion(apellidos))