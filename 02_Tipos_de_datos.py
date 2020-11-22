# Entero.
edad = 15
print(edad)

# Flotante.
numero = 2.5
print(numero)

# Cadena.
nombre = "Juan"
print(nombre)

# Convertir tipos de datos.
print("Hola, me llamo " + nombre)
print("Tengo " + str(edad) + " años")

fecha = int(input("¿En que año estamos?"))
edad = int(input("¿Cuantos años tienes o vas a cumplir este año?"))
nacimiento = fecha - edad
print("Has nacido en el año " + str(nacimiento))

print("*************************")
print("*                       *")
print("* CALCULA LA NOTA MEDIA *")
print("*                       *")
print("*************************")
print()
print("Dime tus tres notas.")
print()
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3) / 3
print("Tu nota media es: " + str(media))
