from tkinter import *

ventana = Tk()
ventana.title("Jesús | Master en Python")
ventana.geometry("700x700")

# Creación del marco (dondeCargar, tamañoAncho, tamañoAlto)
marco_padre = Frame(ventana, width=250, height=250)
# Empaquetar marco dentro de la ventana
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)  # fill= Rellena / expand= Amplia el texto

# Creación del marco_padre (dondeCargar, tamañoAncho, tamañoAlto)
marco = Frame(marco_padre, width=250, height=250)
# Configuración del marco
marco.config(
    bg="red",       # Fondo rojo
    bd=5,           # TamañoBorde en pixeles
   #relief="solid"  # Relieve solido
    relief=SOLID    # Relieve solido de otra manera
)
# Empaquetar marco dentro de la ventana
marco.pack(side=LEFT, anchor=SW)  # Side=LEFT = Posiciona a la izq. el marco

# Evita que se contraiga el marco al añadir texto
marco.pack_propagate(FALSE)
# Añade texto dentro del marco (dondeCargar, textoCargar)
texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",           # Fondo rojo
    fg="white",         # Texto blanco
    font=("Arial",20)   # Fuente de letra y tamaño
    #Comprobamos la expansión del texto de fill y expand
    #bd=3,
    #relief=SOLID
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)  # fill= Rellena / expand= Amplia el texto

# Creación del marco (dondeCargar, tamañoAncho, tamañoAlto)
marco = Frame(marco_padre, width=250, height=250)
# Configuración del marco
marco.config(
    bg="green",     # Fondo verde
    bd=5,           # TamañoBorde en pixeles
   #relief="solid"  # Relieve solido
    relief=SOLID    # Relieve solido de otra manera
)
# Empaquetar marco dentro de la ventana
marco.pack(side=RIGHT, anchor=SE)  # Side=RIGHT = Posiciona a la der. el marco

# Creación del marco_padre (dondeCargar, tamañoAncho, tamañoAlto)
marco_padre = Frame(ventana, width=250, height=250)
# Empaquetar marco dentro de la ventana
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)  # fill= Rellena / expand= Amplia el texto

# Creación del marco (dondeCargar, tamañoAncho, tamañoAlto)
marco = Frame(marco_padre, width=250, height=250)
# Configuración del marco
marco.config(
    bg="blue",      # Fondo azul
    bd=5,           # TamañoBorde en pixeles
   #relief="solid"  # Relieve solido
    relief=SOLID    # Relieve solido de otra manera
)
# Empaquetar marco dentro de la ventana
marco.pack(side=LEFT)  # Side=LEFT = Posiciona a la izq. el marco

# Creación del marco (dondeCargar, tamañoAncho, tamañoAlto)
marco = Frame(marco_padre, width=250, height=250)
# Configuración del marco
marco.config(
    bg="orange",    # Fondo anaranjado
    bd=5,           # TamañoBorde en pixeles
   #relief="solid"  # Relieve solido
    relief=SOLID    # Relieve solido de otra manera
)
# Empaquetar marco dentro de la ventana
marco.pack(side=RIGHT)  # Side=RIGHT = Posiciona a la der. el marco

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()