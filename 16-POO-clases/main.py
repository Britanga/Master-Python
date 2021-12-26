# Programación orientada a objetos (POO o OOP)

# Definir una clase (molde para crear más objetos de ese tipo
# (Coche) con características similares)

class Coche:

    # Atributos o propiedades (variables)
    # Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):  # Setter: Introduce/Cambia datos
        self.color = color

    def getColor(self):         # Getter: Muestra datos
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):         # Parámetro self para acceder a los atributos
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
# Fin definición clase

# Crear objetos / instanciar la clase
coche = Coche()                                     # Invocamos a la clase Coche

print("COCHE 1: ")

coche.setColor("amarillo")                          # Introduce/Cambia datos usando setter
coche.setModelo("Murcielago")

print(coche)                                        # Muestra que es un objeto
print(coche.marca)                                  # Muestra atributo del objeto
print(coche.marca, coche.color)                     # Muestra atributos del objeto
#print("Velocidad actual: ", coche.velocidad)
print("Velocidad actual: ", coche.getVelocidad())   # Muestra datos usando getter
print(coche.marca, coche.getModelo(), coche.getColor())

coche.acelerar()                                    # Ejecución de los métodos
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad()) # Comprueba ejecución de los métodos

print("--------------------------------")

# Crear más objetos
coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("COCHE 2: ")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))                             # Comprueba que en efecto, es una clase