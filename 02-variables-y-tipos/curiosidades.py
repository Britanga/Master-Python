mi_texto = '"Master"'
mi_texto2 = "en \"Python\"" # Usando diagonal se anula la función del siguiente caracter

texto_unido = mi_texto + " " + mi_texto2 # Espaciado
print(texto_unido)


texto_unido = mi_texto + " \n " + mi_texto2 # Salto de linea
print(texto_unido)


texto_unido = mi_texto + " \t " + mi_texto2 # Tabulador
print(texto_unido)


texto_unido = mi_texto + " \r " + mi_texto2 # Borra todas las variables de la izquierda
print(texto_unido)