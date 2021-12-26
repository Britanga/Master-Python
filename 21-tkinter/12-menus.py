from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

# Crea objeto Menu en "mi_menu"
mi_menu = Menu(ventana)
# Indica que va a cargar un menú (atributo "menu"= objeto "mi_menu")
ventana.config(menu=mi_menu)

# Crea objeto Menu en "archivo"
archivo = Menu(mi_menu, tearoff=0)  # tearoff=0 quita linea separadora del principio
# Opciones del submenú
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)    # Ejecuta función salir

# Opciones del menú
mi_menu.add_cascade(label="Archivo", menu=archivo)          # Añade submenú archivo
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccionar")

ventana.mainloop()