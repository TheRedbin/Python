user_option = input("¿Piedra, Papel o Tijera? -> ")
computer_option = "Papel"

if user_option == computer_option:
    print("Empate")
elif user_option == "Piedra":
	if computer_option == "Tijera":
		print("Piedra gana a Tijera")
		print("User Gana")
	else:
		print("Papel gana a Piedra")
		print("Computer gana")
elif user_option == "Papel":
	if computer_option == "Piedra":
		print("Papel gana a Piedra")
		print("User gana")
	else:
		print("Tijeras gana a Papel")
		print("Computer gana")
elif user_option == "Tijera":
	if computer_option == "Papel":
		print("Tijera gana a Papel")
		print("User gana")
	else:
		print("Piedra gana a Tijera")
		print("Computer gana")