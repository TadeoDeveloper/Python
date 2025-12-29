import random # Libreria para generar numeros aleatorios

print("===================Rock Paper Scissors===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int(input("Selecciona un numero del 1 al 3: "))
computer = random.randint(1, 3)
print("Tu eleccion:", player)
print(f"La computadora escogio: {computer}")

# Logica del juego
if player == 1 and computer == 1:
    print("Empate")
elif player == 2 and computer == 2:
    print("Empate")
elif player == 3 and computer == 3:
    print("Empate")
elif player == 1 and computer == 3: 
    print("Gano el jugador")
elif player == 2 and computer == 1:
    print("Gano el jugador")
elif player == 3 and computer == 2:
    print("Gano el jugador")
elif computer == 1 and player == 3: 
    print("Gano la computadora")
elif computer == 2 and player == 1:
    print("Gano la computadora")
elif computer == 3 and player == 2:
    print("Gano la computadora")
else:
    print("Porfavor introduzca un numero valido. ")
