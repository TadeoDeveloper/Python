# Variables globales
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Bienvenido al test de Hogwarts")

# Entrada de datos
print("Q1) Do you like Dawn or Dusk? 1) Dawn 2) Dusk")
pregunta_1 = int(input(""))
print("Q2) When I'm dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold")
pregunta_2 = int(input(""))
print("Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum")
pregunta_3 = int(input(""))

if pregunta_1 == 1:
    Gryffindor += 1
    print("Gryffindor: ", Gryffindor)
    Ravenclaw += 1
    print("Ravenclaw: ", Ravenclaw)
elif pregunta_1 == 2:
    Hufflepuff += 1
    print("Hufflepuff: ", Hufflepuff)
    Slytherin += 1
    print("Slytherin: ", Slytherin)

if pregunta_2 == 1:
    Hufflepuff += 2
    print("Hufflepuff: ", Hufflepuff)
elif pregunta_2 == 2:
     Slytherin += 2
     print("Slytherin: ", Slytherin)
elif pregunta_2 == 3:
    Ravenclaw += 2
    print("Ravenclaw: ", Ravenclaw)
elif pregunta_2 == 4:
    Gryffindor += 2
    print("Gryffindor: ", Gryffindor)

if pregunta_3 == 1:
    Slytherin += 4
    print("Slytherin: ", Slytherin)
elif pregunta_3 == 2:
    Hufflepuff += 4
    print("Hufflepuff: ", Hufflepuff)
elif pregunta_3 == 3:
    Ravenclaw += 4
    print("Ravenclaw: ", Ravenclaw)
elif pregunta_3 == 4:
    Gryffindor += 4
    print("Gryffindor: ", Gryffindor)
else:
    print("Respuesta inválida")


