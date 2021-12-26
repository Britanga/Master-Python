from tkinter import *           # De tkinter importar todo
from PIL import Image, ImageTk  # De pillow importar Image=carga imagen y ImageTk=carga imagen dentro de Tkinter

# Crear la ventana raiz
ventana = Tk()
ventana.geometry("700x500") # 700Horizontal 500Vertival

# 1erParametro=dondeCargar / 2doParámetro=textoCargar
Label(ventana, text="Hola, soy Jesús!!").pack(anchor=W)
# pack=Empaquetar texto dentro de la ventana / anchor = orientación del texto

# Cargar imagen en variable "imagen"
imagen = Image.open('./21-tkinter/imagenes/lobo-gris.jpg')
# Renderiza imagen en tkinter
render = ImageTk.PhotoImage(imagen)

# Cargar imagen dentro de un label
# 1erParametro=dondeCargar / 2doParámetro=imagenCargar
Label(ventana, image=render).pack(anchor=E)
# pack=Empaquetar imagen dentro de la ventana / anchor = orientación de la imagen

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()