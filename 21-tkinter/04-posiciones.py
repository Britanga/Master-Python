from tkinter import *

# Crear la ventana raiz
ventana = Tk()

# Asigna tamaño de ventana
#ventana.geometry("700x500") # 700Horizontal 500Vertical

# 1erParametro=dondeCargar / 2doParámetro=textoCargar
texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
            fg="white",             # Texto en blanco
            bg="black",             # Fondo en negro
            padx=50,                # Margen horizontal
            pady=20,                # Margen vertical
            font=("Consolas", 30)   # Fuente de letra y tamaño
)
# Empaquetar texto dentro de la ventana
texto.pack(side=TOP)    # Side=TOP = Centra el texto

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
texto.pack(side=TOP, fill=X, expand=YES)    # fill= Rellena / expand= Amplia el texto

texto = Label(ventana, text="Basico 1")
texto.config(           # Estilo del texto
    #justify=RIGHT      # Justificación del texto
    height=3,           # Altura en lineas de texto (no pixeles)
    bg="green",         # Fondo en verde
    font=("Arial",18),  # Fuente de letra y tamaño
    padx=10,            # Margen horizontal
    pady=10,            # Margen vertical
    cursor="spider"     # Forma de araña el cursor estando encima del texto
)
texto.pack(side=LEFT, fill=X, expand=YES)   # Texto a la izq.

texto = Label(ventana, text="Basico 2")
texto.config(           # Estilo del texto
    #justify=RIGHT      # Justificación del texto
    height=3,           # Altura en lineas de texto (no pixeles)
    bg="red",           # Fondo en rojo
    font=("Arial",18),  # Fuente de letra y tamaño
    padx=10,            # Margen horizontal
    pady=10,            # Margen vertical
    cursor="spider"     # Forma de araña el cursor estando encima del texto
)
texto.pack(side=LEFT, fill=X, expand=YES)   # Texto a la izq.

texto = Label(ventana, text="Basico 3")
texto.config(           # Estilo del texto
    #justify=RIGHT      # Justificación del texto
    height=3,           # Altura en lineas de texto (no pixeles)
    bg="pink",          # Fondo en rosado
    font=("Arial",18),  # Fuente de letra y tamaño
    padx=10,            # Margen horizontal
    pady=10,            # Margen vertical
    cursor="spider"     # Forma de araña el cursor estando encima del texto
)
texto.pack(side=LEFT, fill=X, expand=YES)   # Texto a la izq.

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()