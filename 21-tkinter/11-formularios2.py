from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
#encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

# Botones check
def mostrarProfesion():
    texto = ""

    if web.get():                           # Si Check de web es True
        texto += "Desarrollo web "          # Concatena este texto

    if movil.get():                         # Si Check de movil es True
        if web.get():                       # Si Check de web es True
            texto += "y Desarrollo movil"   # Concatena este texto
        else:
            texto += "Desarrollo movil"     # Sino, concatena este texto

    # Al pulsar algun check muestra el msj. con fondo verde y letra blanca
    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )

web = IntVar()  # Variables de tipo Tkinter
movil = IntVar()

Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)

Checkbutton(
    ventana,                    # dondeCargar
    text="Desarrollo web",      # textoMostrar
    variable=web,               # Guarda en web
    onvalue=1,                  # Si pulsa el check guarda 1
    offvalue=0,                 # Sino pulsa el check se mantiene en 0
    command=mostrarProfesion    # Si pulsa el check, ejecuta esta función
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)        # Crea etiqueta "mostrar"
mostrar.grid(row=4, column=0)   # Ubica en fila 4 columna 0

# Radio Buttons
def marcar():
    marcado.config(text=opcion.get())   # Actualiza etiqueta con la opcion elegida

opcion = StringVar()            # String porque guarda una serie de caracteres
opcion.set(None)                # Al inciar el programa muestran desmarcados las opciones

Label(ventana, text="¿Cuál es tu género?").grid(row=5)

Radiobutton(
    ventana,                    # dondeCargar
    text="Masculino",           # textoMostrar
    value="Masculino",          # textoGuardar
    variable=opcion,            # Guarda en opcion
    command=marcar              # Si pulsa el check, ejecuta esta función
).grid(row=6)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)        # Crea etiqueta "marcado"
marcado.grid(row=8)             # Ubica en fila 8 columna 0

# Option Menu
def seleccionar():
    seleccionado.config(text=opcion.get())  # Actualiza etiqueta con la opcion elegida

opcion = StringVar()            # String porque guarda una serie de caracteres
opcion.set("Opcion 1")          # Dato por defecto

Label(ventana, text="Selecciona una opción").grid(row=5, column=1)

# (dondeCargar, variableUsando, opciones, opciones, opciones)
select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)   # Crea etiqueta "seleccionado"
seleccionado.grid(row=8, column=1)

ventana.mainloop()