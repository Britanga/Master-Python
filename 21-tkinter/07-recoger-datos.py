from tkinter import *

# Crear la ventana raiz
ventana = Tk()
# Cambio en el tamaño de la ventana
ventana.geometry("700x700")
ventana.config(
    bd=50       # TamañoBorde en pixeles
    #bg="#ccc"   # Fondo gris claro
)

# Devuelve resultado
def getDato():
    resultado.set(dato.get())   
    # Set permite darle a un StringVar un valor
    # recoge el dato de "dato" y muestra el valor en "resultado"
    # Es necesario usar esta función para mostrar los textos introducidos

    # Si hay datos en resultado ejecuta los estilos
    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="green",     # Fondo verde
            fg="white"      # Texto blanco
        )

# Crea variables
dato = StringVar()          # Declara variable de tipo cadena en Tkinter
resultado = StringVar()

# Mostrar texto en el programa
Label(ventana, text="Mete un texto: ").pack(anchor=NW)
# Crea campo de texto y guarda en "dato"
Entry(ventana, textvariable=dato).pack(anchor=NW)

# Mostrar texto en el programa
Label(ventana, text="Dato recogido: ").pack(anchor=NW)
# Muestra el valor de "resultado" que actualiza cuando presiona el boton
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)

# Crea boton que muestra el texto introducido
Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()