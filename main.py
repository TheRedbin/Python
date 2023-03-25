user_option = input("¿Piedra, Papel o Tijera? -> ")
user_option = user_option.lower()
computer_option = "papel"

if user_option == computer_option:
    print("Empate")
elif user_option == "piedra":
	if computer_option == "tijera":
		print("Piedra gana a Tijera")
		print("User Gana")
	else:
		print("Papel gana a Piedra")
		print("Computer gana")
elif user_option == "papel":
	if computer_option == "piedra":
		print("Papel gana a Piedra")
		print("User gana")
	else:
		print("Tijeras gana a Papel")
		print("Computer gana")
elif user_option == "tijera":
	if computer_option == "papel":
		print("Tijera gana a Papel")
		print("User gana")
	else:
		print("Piedra gana a Tijera")
		print("Computer gana")