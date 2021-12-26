cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar
#print(numeros)
numeros.sort()  # Sort ordena los números
#print(numeros)

# Añadir elementos
cantantes.append("Natos y waor")    # Agrega al final
cantantes.insert(1, "David Bisbal") # Agrega en el n° índice que quieras
#print(cantantes)

# Eliminar elementos
cantantes.pop(1)                    # Elimina índice
cantantes.remove('Bad Bunny')       # Elimina elemento
#print(cantantes)

# Dar la vuelta
#print(numeros)
numeros.reverse()
#print(numeros)

# Buscar dentro de una lista
#print('Drake' in cantantes)

# Contar elementos
#print(cantantes)           # Comprobamos
#print(len(cantantes))      # Cuenta

# Cuántas veces aparece un elemento
numeros.append(8)           # Añadimos
#print(numeros.count(8))    # Contamos

# Conseguir índice
# print(cantantes.index("Drake"))   # N° índice que se encuentra el elemento

# Unir listas
cantantes.extend(numeros)   # Unimos dos listas
print(cantantes)            # Comprobamos