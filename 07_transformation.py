name: str = "Michael"
print(type(name))
name: int = 12
print(type(name))
name: bool = True
print(type(name))

print("Michael" + " Manrique")
print(10 + 20)
print("Michael" + "12")

age: int = 25
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

age: int = input("Ingrese su edad: ")
print(type(age))
age: int = int(age)
age += 10
print(f"Su edad en 10 años será: {age}")