"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""
#import usuarios.acciones # Otra manera, pero queda más largo cuando usemos las funciones
from usuarios import acciones   # Del paquete "usuarios" Importa modulo "acciones"

print("""
Acciones disponibles:
    - registro
    - login
""")

# Creamos/Instanciamos objeto de clase "Acciones" con nombre "hazEl"
# Accede a la clase "Acciones" del modulo "acciones" paquete "usuarios"
hazEl = acciones.Acciones()

accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()