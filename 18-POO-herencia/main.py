import clases

# Creamos objeto persona
persona = clases.Persona()

# Introducimos datos
persona.setNombre("Jesús")
persona.setApellidos("Brito")
persona.setAltura("180 cm")
persona.setEdad("800 años")

# Muestra nombre y apellidos que son atributos de clase padre "Persona"
print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar()) # Ejecuta cualquier método de clase padre "Persona"
print("----------------------------------------")

# Creamos objeto informático
informatico = clases.Informatico()

# Introducimos datos
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

# Muestra nombre y apellidos que son atributos de clase padre "Persona" pero,
# son heredados a clase hijo "Informatico"
print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())   # Muestra método de clase hijo "Informatico"
print(informatico.caminar())        # Muestra método de clase padre "Persona"
print(informatico.experiencia)      # Muestra atributo de clase hijo "Informatico"

print("----------------------------------------")

# Creamos objeto Tecnico de Redes
tecnico = clases.TecnicoRedes()

# Introduce datos al setter de clase padre "Persona"
tecnico.setNombre("Jesús")

# Muestra atributo de clase hijo "TecnicoRedes"
# Muestra atributo de clase padre "Persona"
# Muestra atributo del constructor de clase hijo "Informatico"
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())