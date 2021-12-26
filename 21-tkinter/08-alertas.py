from tkinter import *
from tkinter import messagebox as Messagebox    # Importa librería de alertas

# Crear ventana raiz
ventana = Tk()

ventana.config(
    bd=50       # TamañoBorde en pixeles
)

# Muestra alerta
def sacarAlerta():
    # (nombreVentana, infoVentana)
    Messagebox.showinfo("Alerta", "Hola soy Jesús Brito")       # Icono de información
    #Messagebox.showwarning("Alerta", "Hola soy Jesús Brito")   # Icono de advertencia
    #Messagebox.showerror("Alerta", "Hola soy Jesús Brito")     # Icono de error

# Crear boton "Mostrar alerta!!!"
Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

# Muestra pregunta de Yes/No
def salir(nombre):
    resultado = Messagebox.askquestion("Salir","¿Continuar ejecutando la aplicación?")

    if resultado != "yes":
        Messagebox.showinfo("Chao!!", f"Adios {nombre}")  # Msj antes de cerrar ventana
        ventana.destroy()                                 # Cierra la ventana

# Crear boton "Salir"
# lambda evita ejecución de la función al iniciar el programa
Button(ventana, text="Salir", command=lambda: salir("Jesús Brito")).pack()

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()