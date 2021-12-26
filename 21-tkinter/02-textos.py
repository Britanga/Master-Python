from tkinter import *

# Crear la ventana raiz
ventana = Tk()

# Asigna tamaño de ventana
ventana.geometry("700x500") # 700Horizontal 500Vertical

# 1erParametro=dondeCargar / 2doParámetro=textoCargar
texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
            fg="white",             # Texto en blanco
            bg="black",             # Fondo en negro
            padx=50,                # Margen horizontal
            pady=20,                # Margen vertical
            font=("Consolas", 30)   # Fuente de letra y tamaño
)
texto.pack()    # Empaquetar texto dentro de la ventana

texto = Label(ventana, text="Soy Jesús Brito")
texto.config(           # Estilo del texto
    #justify=RIGHT      # Justificación del texto
    height=3,           # Altura en lineas de texto (no pixeles)
    bg="orange",        # Fondo en anaranjado
    font=("Arial",18),  # Fuente de letra y tamaño
    padx=10,            # Margen horizontal
    pady=10,            # Margen vertical
    cursor="spider"     # Forma de araña el cursor estando encima del texto
)
texto.pack(anchor=SE)    # Movimiento del texto

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

#texto = Label(ventana, text="Master en Python")
#texto = Label(ventana, text=pruebas("Jesús", "Brito", "Venezuela"))
# Ventaja: Pasas parámetros desordenados y la función pruebas la ordenará automáticamente
texto = Label(ventana, text=pruebas(pais="Venezuela", apellidos="Brito", nombre="Jesús"))
texto.config(           # Estilo del texto
    #justify=RIGHT      # Justificación del texto
    height=3,           # Altura en lineas de texto (no pixeles)
    bg="green",         # Fondo en verde
    font=("Arial",18),  # Fuente de letra y tamaño
    padx=10,            # Margen horizontal
    pady=10,            # Margen vertical
    cursor="spider"     # Forma de araña el cursor estando encima del texto
)
texto.pack(anchor=NW)    # Movimiento del texto

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()