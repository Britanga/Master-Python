"""
# FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el " + str(contador))
    resultado += contador

print(f"El resultado es: {resultado}")

# Ejemplo tablas de multiplicar
print("\n################# EJEMPLO #################")

numero_usuario = int(input("¿De qué número quiere la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla de multiplicar del número {numero_usuario} ####")

for numero_tabla in range(1,11):

    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos !!")
        break # Finaliza el bucle

    print(f"{numero_usuario} * {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")