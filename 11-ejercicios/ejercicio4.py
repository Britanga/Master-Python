"""
Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string,
un entero y un booleano y que imprima un mensaje
según el tipo de dato de cada variable. Usar funciones
"""

def traducirTipo(tipo):
    result = ""
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"

    return result       # Devuelve un msj más limpio que el predeterminado con Type

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)   # Comprueba si es True o False
    result = ""

    if test:    # Si test es True
        result = f"El tipo de dato es {traducirTipo(tipo)}" # Llama la función de arriba
    else:       # Sino
        result = "El tipo de dato no es correcto"

    return result       # Indica si el tipo de dato es correcto y cual es

mi_lista = ["Hola mundo", 77]
titulo = "Master en Python"
numero = 20
verdadero = True

print(comprobarTipado(mi_lista, list))  # Imprime la función en las 4 variables
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))