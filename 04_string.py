name: str = "Muchael"
last_name: str = "Manrique"
print(name)
print(last_name)

full_name: str = name + " " + last_name
print(full_name)

quote: str = "I'm Michael"
print(quote)

dog: str = '"El perro"'
print(dog)

# format

template: str = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template: str = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', template)

template: str = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)
print(type(template))