# Tkinter
# Modulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

# Es mejor una clase con todas las funciones dentro, q las funciones x separado
# Contiene 1 constructor y 3 funciones (cargar, addTexto y mostrar)
class Programa:
    def __init__(self):
        self.title = "Master en Python con Victor Robles"
        self.icon = './imagenes/logotipo.ico'
        self.icon_alt = './21-tkinter/imagenes/logotipo.ico'
        self.size = "770x470"   # 770Horizontal 470Vertival
        self.resizable = False

    def cargar(self):   # Para tener acceso a todas las variables
        # Crear la ventana raiz
        ventana = Tk()
        # Convertir en variable self
        self.ventana = ventana

        # Título de la ventana
        #ventana.title("Interfaz gráfica con Python y Victor Robles")
        ventana.title(self.title)

        # Comprobar si existe un archivo de ruta absoluta usando libreria os.path metodo isfile
        #ruta_icono = os.path.abspath('./imagenes/logotipo.ico')
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):  # Si no encuentra ruta_icono, cambia ruta relativa
            #ruta_icono = os.path.abspath('./21-tkinter/imagenes/logotipo.ico')
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        #ventana.iconbitmap("./21-tkinter/imagenes/logotipo.ico")    #./ es ruta relativa
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        # 1erParametro=dondeCargar / 2doParámetro=textoCargar
        texto = Label(ventana, text=ruta_icono)
        texto.pack()    # Empaquetar texto dentro de la ventana

        # Cambio en el tamaño de la ventana
        #ventana.geometry("750x450")
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:  # Si resizable es True ejecuta instrucción de abajo
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        #ventana.resizable(0,0) # Bloquea todas las esquinas
        #ventana.resizable(1,1) # Permite modificar tamaño de ventana
        #ventana.resizable(1,0)  # Modifica solo de manera horizontal
        #ventana.resizable(1,0)  # Modifica solo de manera vertical

        # Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
        #ventana.mainloop()

    def addTexto(self, dato):
        #texto = Label(self.ventana, text="Hola desde un método")
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
        self.ventana.mainloop()

# Crea objeto "programa" de clase "Programa"
programa = Programa()

# Llama función "cargar" de objeto "programa"
programa.cargar()

# Llama función "addTexto" de objeto "programa"
programa.addTexto("Hola")
programa.addTexto("soy un texto")
programa.addTexto("Bienvenido al master en Python")
programa.addTexto("Soy jesús brito")
programa.addTexto("Sigueme en youtube")

# Llama función "mostrar" de objeto "programa"
programa.mostrar()