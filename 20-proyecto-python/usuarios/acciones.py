import usuarios.usuario as modelo # Importa el modelo "usuario" de paquete "usuarios" con un alias "modelo" en vez de usar "usuarios.usuario"
import notas.acciones    # Para poder usar las acciones de notas, se importa en este modulo principal "acciones.py" de paquete "usuarios", xq así se encadena la llamada con los otros métodos

# Es mejor una clase con todas las funciones dentro, q las funciones x separado
# Contiene 3 funciones (registro, login y proximasAcciones)
class Acciones:     

    # Registra usuario actual en la BD
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")

        # Guarda datos del usuario
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # Creamos/Instanciamos objeto de clase "Usuario" con nombre "usuario"
        # Introduce los datos del usuario al constructor de la clase "Usuario" del modulo "usuario" paquete "usuarios"
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        # Registrar objeto "usuario" en la BD
        # Ejecuta la función registrar de la clase "Usuario" del modulo "usuario" paquete "usuarios"
        registro = usuario.registrar()

        if registro[0] >= 1:    # Si el n° registro es >= 0, significa q ha registrado
            print(f"\nPerfecto {registro[1].nombre} te haz registrado con el email {registro[1].email}")
            # El índice de registro siempre es 1, xq 1 es el rowcount (n° registro guardados)
        else:
            print("\nNo te haz registrado correctamente!!!")

    # Inicia sesión, si es correcto ejecuta("msj de bienvenida" y "muestra proximasAcciones")
    def login(self):
        print("\nVale!! Identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            # Crear objeto para Obtener email y contraseña
            # Introduce email y contraseña a clase "Usuario" del modulo "usuario" paquete "usuarios"
            usuario = modelo.Usuario('', '', email, password)
            # Llama a la función identificar (comprueba si email existe y si contraseña es correcta)
            login = usuario.identificar()

            if email == login[3]:   # Si email = email q devuelve la consulta
                print(f"\nBienvenido {login[1]}, te haz registrado en el sistema el {login[5]}")
                # Llama al método para preguntar ¿Qué quieres hacer? después de logearse correctamente
                self.proximasAcciones(login)

        except Exception as e:  # Exception captura los errores y ejecuta las sig. instrucciones
            print(type(e))          # Muestra el error.         Ejm: <class 'TypeError'>
            print(type(e).__name__) # Muestra nombre del error. Ejm: TypeError
            print(f"Login incorrecto!! Intentalo más tarde")    # Muestra msj.

    # Asistente de próximos pasos
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")

        # Creamos/Instanciamos objeto de clase "Acciones" con nombre "hazEl"
        # Declara variable "hazEl" llama a la clase "Acciones" del modulo "acciones" paquete "notas"
        hazEl = notas.acciones.Acciones()

        # Condicionales si el usuario escribe "crear", "mostrar", "eliminar" o "salir"
        if accion == "crear":
            hazEl.crear(usuario)    # Llama método "crear" dentro de clase "Acciones" del paquete "notas" con parámetro "usuario" para poder usar los datos de "usuario" de la BD
            #print("Vamos a crear") # Manera sin usar "acciones.py" del paquete "notas"
            self.proximasAcciones(usuario)  # Sigue preguntando hasta q usuario use "salir"
        elif accion == "mostrar":
            hazEl.mostrar(usuario)  # Manera llamar método "mostrar" dentro de clase "Acciones" del paquete "notas" con parámetro "usuario" para poder usar los datos de "usuario" de la BD
            #print("Vamos a mostrar")
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)   # Manera llamar método "borrar" dentro de clase "Acciones" del paquete "notas" con parámetro "usuario" para poder usar los datos de "usuario" de la BD
            #print("Vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!!!")  # índice 1= nombre del usuario
            exit()  # Corta la ejecución del programa