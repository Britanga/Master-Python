"""
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minuscula y mostrarlo
en mayusculas.
"""

texto = ""

if len(texto.strip()) <= 0:     # Si esta vacía quitando los espacios en blanco
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")