import os       # Crear, comprobar, eliminar carpetas
import shutil   # Copia, renombra, elimina archivos

# Crear carpeta
if not os.path.isdir("./mi_carpeta"): # Si no existe "./mi_carpeta"
    os.mkdir("./mi_carpeta")          # Crear "'/mi_carpeta"
else:
    print("Ya existe el directorio")

# Eliminar carpeta
#os.rmdir('./mi_carpeta')

# Copiar carpeta
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
shutil.copytree(ruta_original, ruta_nueva)
"""

# Eliminar carpeta
#os.rmdir('./mi_carpeta_COPIADA')

print("Contenido de mi carpeta:")
contenido = os.listdir("./mi_carpeta")  # Crea una lista
print(contenido)                        # Muestra toda la carpeta en forma de lista

for fichero in contenido:               # Muestra cada fichero de mi_carpeta
    print("Fichero: " + fichero)