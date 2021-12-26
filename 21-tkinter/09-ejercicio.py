"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Jesús Brito")
ventana.geometry("400x400")
ventana.config(bd=25)

# Definir funciones
def cfloat(numero): # Devuelve el valor de numero1 y numero2 a flotantes
    try:
        result = float(numero)
    except: # Captura el error, result=0 y muestra el sig. msj
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")
    
    return result

def sumar():
    # Actualiza resultado con set ya que es StringVar y get obtiene los valores
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(cfloat(numero1.get()) - cfloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(cfloat(numero1.get()) * cfloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(cfloat(numero1.get()) / cfloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")
    # Actualiza y deja vacio las variables
    numero1.set("")
    numero2.set("")

# Variables tipo Tkinter
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

# 1 Marco (dondeCargar, ancho, alto)
marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
#Evita que se deforme el marco
marco.pack_propagate(False)

# 2 Etiquetas y 2 campos de texto
Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

# Etiqueta espaciadora
Label(marco, text="").pack()

# 4 Botones
Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()