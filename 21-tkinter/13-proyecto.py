"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, Añadir, Información, Salir)
- Opción de salir
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
"""

from tkinter import *
from tkinter import ttk # Importa un mejor marco

# Ventana
ventana = Tk()
# Tamaño fijo
#ventana.geometry("500x500")
# Tamaño mínimo (Se ajusta al tamaño dependiendo de la pantalla)
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter - Master en Python")
# No redimensionable
ventana.resizable(0,0)

# Diferentes pantallas
def home():

    # Estilos de Etiqueta
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=20
    )
    # Ubicación de Etiqueta
    home_label.grid(row=0, column=0)
    
    # Cargar marco
    products_box.grid(row=2)

    # Mostrar datos listados en la pantalla home
    """
    for product in products:
        if len(product) == 3:
            product.append("added") # +1elemento para que no se repita el mismo producto
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="--------------").grid()
    """
    for product in products:
        if len(product) == 3:
            product.append("added") # +1elemento para que no se repita el mismo producto
            products_box.insert('', 0, text=product[0], values = (product[1]))

    # Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def add():

    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10) # columnspan para poder mostrar entry

    # Campos del Formulario de añadir productos
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(   # Para reducir el tamaño
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def info():
    
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    add_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()
    return True

def add_product():
    # Guardar datos temporalmente
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")   # Parametros especiales obligatorios
    ])

    # Limpiar campos
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    # Dirige a pantalla Home
    home()

# Variables
products = []   # Tipo array en Tkinter
name_data = StringVar()
price_data = StringVar()

# Etiqueta Inicio
home_label = Label(ventana, text="Inicio")
# Marco
#products_box = Frame(ventana, width=250)

# Mejor marco
Label(ventana).grid(row=1)  # Separador
products_box = ttk.Treeview(height=12, columns=2)   # Cargar tabla llamada "products_box"
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Producto', anchor=W)
products_box.heading("#1", text='Precio', anchor=W)

# Formulario de añadir productos
# Etiqueta Añadir
add_label = Label(ventana, text="Añadir producto")
# Marco
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")        # Etiqueta del formulario
add_name_entry = Entry(add_frame, textvariable=name_data) # Campo del formulario

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame) # Linea separadora

# Guardar datos temporalmente
boton = Button(add_frame, text="Guardar", command=add_product)  # Vincular funcion guardar

# Etiquetas Información
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Jesús Brito - 2021")

# Cargar pantalla Incio
home()

# Un menu (Inicio, Añadir, Información, Salir)
menu_superior = Menu(ventana)
# Entradas del menú
menu_superior.add_command(label="Inicio", command=home)   # Vincular funciones
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)  # Opción de salir
# Cargar menú
ventana.config(menu=menu_superior)

# Arrancar y mostrar la ventana hasta que se cierre (importante sea el último)
ventana.mainloop()