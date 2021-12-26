from coche import Coche     # Importando la clase "Coche" del modulo "coche.py"

# Usamos el constructor (Así creamos muchos objetos con datos diferentes)
carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

# Muestra todo con getter
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
carro3 = "String aleatorio" # Al cambiar de clase a string el Else muestra el msj.
if type(carro3) == Coche:   # Comprueba si carro3 es el mismo tipo de dato que Coche
    print("Es un objeto correcto !!")
else:
    print("No es un objeto!!")

# Visibilidad
print(carro.soy_publico)    # Muestra atributo público
print(carro.getPrivado())   # Muestra atributo privado
"""Nota: los atributos privados sirven para propiedades q solo queremos que esten
dentro de la clase y que no se puedan leer desde fuera """