"""Herencia: Es la posibilidad de compartir atributos y métodos
entre clases. Y que diferentes clases hereden de otras"""

class Persona:          # Clase Padre
    """
    nombre
    apellidos
    altura
    edad
    """
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona): # Clase hijo "Informatico" que hereda de la clase padre "Persona"
    """
    lenguajes
    experiencia
    """

    def __init__(self):     # Constructor (Son exclusivos en cada clase)
        self.lenguajes = "HTML, CSS, Javascript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):  # Setter
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado tu ordenador"

class TecnicoRedes(Informatico):    # Hereda tanto de "informatico" como de "persona"
    
    def __init__(self):     # Contructor
        # Accede a constructor tanto de clase hijo "Informatico" como de clase padre "Persona"
        super().__init__()  # Invoca "__init__" (Constructor) de super() que es clase padre
        self.auditarRedes = 'experto'   # Definiendo propiedades/atributos
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"