"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION          AVENTURA                DEPORTES
GTA             ASSINS                  FIFA 21
COD             CRASH                   PRO 21
PUGB            Prince of persia        MOTO GP 21

Mostrar esta información ordenada
"""

tabla = [
    {
        "categoria" : "ACCION",
        "juegos" : ["GTA", "Call of Duty", "PUGB"]
    },
    {
        "categoria" : "AVENTURA",
        "juegos" : ["ASSASINS", "Crash Bandicoot", "Prince of persia"]
    },
    {
        "categoria" : "DEPORTES",
        "juegos" : ["FIFA 21", "PES 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"---------- {categoria['categoria']} ----------")
    for juego in categoria['juegos']:
        print(juego)