from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Jesús Brito")

# Texto encabezado
encabezado = Label(ventana, text="Encabezado con Tkinter - Jesús Brito")
encabezado.config(
    fg="white",             # Texto blanco
    bg="darkgray",          # Fondo gris oscuro
    font=("Open sans",18),  # Fuente de letra y tamaño
    padx=10,                # Margen horizontal
    pady=10                 # Margen vertical
)
# Usar grid en lugar de side y anchor
# (fila, columna, crea12columnas, pegado a la izq.)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)
#encabezado.pack(side=LEFT, anchor=NW)   # Side=LEFT = Posiciona a la izq. el marco

# Label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
# Usar grid en lugar de side y anchor
# (fila, columna, pegado a la izq., margenHorizontal, margenVertical)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
# justify = OrientacionDelTipeo / state = campo bloqueado o desbloqueado
campo_texto.config(justify="right", state="normal")

# Label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto (apellidos)
campo_texto = Entry(ventana)
# Usar grid en lugar de side y anchor
# (fila, columna, pegado a la izq., margenHorizontal, margenVertical)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
# justify = OrientacionDelTipeo / state = campo bloqueado o desbloqueado
campo_texto.config(justify="left", state="normal")

# Label para el campo (descripcion)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo de texto grande (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)

campo_grande.config(
    width=30,               # width = Tamaño de ancho
    height=5,               # height = Altura en lineas de texto (no pixeles)
    font=("Arial", 12),     # Fuente de letra y tamaño
    padx=15,                # Margen horizontal
    pady=15                 # Margen vertical
)

# Label espaciador
Label(ventana).grid(row=4, column=1)

# Boton
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="green", fg="white")

ventana.mainloop()