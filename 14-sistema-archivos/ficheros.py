from io import open # Abrir, escribir, cerrar, leer ficheros
import pathlib      # Ruta absoluta
import shutil       # Copia, renombra, elimina archivos

# Abrir archivos
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"    # Ruta absoluta + fichero
archivo = open(ruta, "a+")          # "a+" es un permiso para crear el .txt

# Escribir
archivo.write("***** Soy un texto metido desde python *****\n")

# Cerrar
archivo.close() # Cada archivo abierto es importante cerrarlo al terminar

# Abrir archivos otra vez
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")   # "r" es un permiso para leer el .txt

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)   # Muestra todo el fichero

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
#print(lista)       # Muestra toda la lista

for frase in lista:              # Recorre cada frase de la lista
    #lista_frase = frase.split() # Guarda c/frase en una lista, y c/índice se separa
    #print(lista_frase)          # por c/espacio en blanco
    print("- " + frase.center(100)) # Centra automáticamente c/frase
    # Nota: lo importante es saber que existen esas funciones para los string

# Copiando archivo en la misma carpeta
# Creamos 2 variables ruta_original y ruta_nueva para hacer el copiado
"""ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)  # Izq. quiero copiar, Der. donde copiar"""

# Copiando archivo en una carpeta diferente
ruta_alternativa = "../07-ejercicios/fichero_copiado77.txt" # Sale de la actual y entra a otra
#shutil.copyfile(ruta_original, ruta_alternativa)

#Nota: ruta absoluta + fichero siempre tiene que tener un "/" al principio el fichero

# Mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_nueva)  # Izq. quiero eliminar, Der. nuevo fichero
"""

# Eliminar
import os
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""

# Comprobar si existe
import os.path

#print(os.path.abspath("./")) # igual a str(pathlib.Path().absolute())
# Ruta absoluta es más seguro
ruta_comprobar = os.path.abspath("./") + "/fichero_texto55.txt"
# Ruta relativa es más sencilla, pero menos segura (siempre comienza con "./")
ruta_comprobar = "./ficheros.py"    # El "." significa directorio actual

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")