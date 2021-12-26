import notas.nota as modelo # Importa el modelo "nota" de paquete "notas" con un alias "modelo" en vez de usar "notas.nota"

# Contiene 3 funciones (crear, mostrar y borrar)
class Acciones:

    # Crea notas del usuario actual en la BD
    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota...")

        # Guarda datos del usuario
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        # Creamos/Instanciamos objeto de clase "Nota" con nombre "nota"
        # Introduce titulo y descripcion al constructor de la clase "Nota" del modulo "nota" paquete "notas"
        nota = modelo.Nota(usuario[0], titulo, descripcion) # usuario[0] = "id" tabla "usuarios"
        # Registrar objeto "nota" en la BD
        # Ejecuta la función guardar de la clase "Nota" del modulo "nota" paquete "notas"
        guardar = nota.guardar()

        # Si el n° registro es >= 0, significa q ha guardado
        if guardar[0] >= 1:
            print(f"\nPerfecto haz guardado la nota: {nota.titulo}")
            """ En lugar de {guardar[1]} también se puede {nota.titulo}
            recomendable sería getter y setter a c/u atributos
            (pero como son atributos públicos se puede de la manera actual)"""
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    # Muestra todas las notas del usuario actual en la BD
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aquí tienes tus notas: ")

        # Creamos/Instanciamos objeto de clase "Nota" con nombre "nota"
        # Introduce "id" tabla "usuarios" a la clase "Nota" del modulo "nota" paquete "notas"
        nota = modelo.Nota(usuario[0])   # usuario[0] = "id" tabla "usuarios"

        # Creo variable "notas" q guarda funcion "listar" q Devuelve todas las notas del usuario actual de la BD
        notas = nota.listar()

        # Muestra lista con todas las tuplas (pero queda mejor con el for de abajo)
        #print(notas)
        
        # Reccore todas las notas y en c/iteración muestra titulo y descripcion de c/nota creadas x usuario actual en la BD
        for nota in notas:
            print("\n******************************************")
            print(nota[2]) # Parámetro 2 = título
            print(nota[3]) # Parámetro 3 = descripcion
            print("******************************************")

    # Borra la nota elegida del usuario actual en la BD
    def borrar(self, usuario):
        print(f"\nOkey {usuario[1]}!! Vamos a borrar notas")

        # Obtiene titulo del usuario a borrar
        titulo = input("Introduce el titulo de la nota a borrar: ")

        # Creamos/Instanciamos objeto de clase "Nota" con nombre "nota"
        # Introduce "id" tabla "usuarios" y el "titulo" tabla "notas" a la clase "Nota" del modulo "nota" paquete "notas"
        nota = modelo.Nota(usuario[0], titulo) # usuario[0] = "id" tabla "usuarios"
        # Eliminar objeto "nota" de la BD
        eliminar = nota.eliminar()

        # Comprueba si borro la nota
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota, prueba luego...")