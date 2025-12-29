# Variables para almacenar los puntos en un diccionario
puntuaciones = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

print("¡Bienvenido al test de Hogwarts! 🧙‍♂️✨")

# Pregunta 1
print("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk")
respuesta1 = int(input("Respuesta (1-2): "))

if respuesta1 == 1:
    puntuaciones["Gryffindor"] += 1
    puntuaciones["Ravenclaw"] += 1
elif respuesta1 == 2:
    puntuaciones["Hufflepuff"] += 1
    puntuaciones["Slytherin"] += 1
else:
    print("Respuesta inválida en la pregunta 1.")

# Pregunta 2
print("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")
respuesta2 = int(input("Respuesta (1-4): "))

if respuesta2 == 1:
    puntuaciones["Hufflepuff"] += 2
elif respuesta2 == 2:
    puntuaciones["Slytherin"] += 2
elif respuesta2 == 3:
    puntuaciones["Ravenclaw"] += 2
elif respuesta2 == 4:
    puntuaciones["Gryffindor"] += 2
else:
    print("Respuesta inválida en la pregunta 2.")

# Pregunta 3
print("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum")
respuesta3 = int(input("Respuesta (1-4): "))

if respuesta3 == 1:
    puntuaciones["Slytherin"] += 4
elif respuesta3 == 2:
    puntuaciones["Hufflepuff"] += 4
elif respuesta3 == 3:
    puntuaciones["Ravenclaw"] += 4
elif respuesta3 == 4:
    puntuaciones["Gryffindor"] += 4
else:
    print("Respuesta inválida en la pregunta 3.")

# Mostrar puntajes
print("\nResultados finales:")
for casa, puntos in puntuaciones.items():
    print(f"{casa}: {puntos} puntos")

# Encontrar la casa con más puntos
casa_ganadora = max(puntuaciones, key=puntuaciones.get)
print(f"\n¡Tu casa es: {casa_ganadora}! 🏆 ¡Felicidades!")
