"""
Refactorizar calculadora creando clases y objetos
"""

from tkinter import *
from tkinter import messagebox

# Es mejor una clase con todas las funciones dentro, q las funciones x separado
# Contiene 1 constructor y 6 funciones (cfloat, sumar, restar, multiplicar, dividir y mostrarResultado)
class Calculadora:

    # Definir constructor para crear las variables
    def __init__(self, alertas):
        # Variables tipo Tkinter
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        # alertas es messagebox
        self.alertas = alertas

    # Definir funciones
    def cfloat(self, numero): # Devuelve el valor de numero1 y numero2 a flotantes
        try:
            result = float(numero)
        except: # Captura el error, result=0 y muestra el sig. msj
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos")
        
        return result

    def sumar(self):
        # Actualiza resultado con set ya que es StringVar y get obtiene los valores
        self.resultado.set(self.cfloat(self.numero1.get()) + self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.cfloat(self.numero1.get()) - self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cfloat(self.numero1.get()) * self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cfloat(self.numero1.get()) / self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operación es: {self.resultado.get()}")
        # Actualiza y deja vacio las variables
        self.numero1.set("")
        self.numero2.set("")

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter | Jesús Brito")
ventana.geometry("400x400")
ventana.config(bd=25)

# Creamos objeto "calculadora" de la clase "Calculadora"
calculadora = Calculadora(messagebox) # Necesario el parámetro para poder usar messagebox

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
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

# Etiqueta espaciadora
Label(marco, text="").pack()

# 4 Botones
Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()