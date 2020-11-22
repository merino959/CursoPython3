# Las variables pueden almacenar valores numericos.
tomates = 10
pimientos = 7
# Tambien pueden almacenar variables.
verduras = tomates + pimientos
print(verduras)

caramelos = 5
precio = 2
coste = caramelos * precio
print(coste)

ahorros = 15
ingresos = 0
gastos = 0
ingresos = ingresos + 10
gastos = gastos + 2
ingresos = ingresos + 8
gastos = gastos + 12
ingresos = ingresos + 5
gastos = gastos + 7
ahorros = ahorros + ingresos - gastos
print(ahorros)

# Tambien pueden almacenar valores logicos (True, False).
alumnos = 30
sillas = 30
aula_completa = alumnos == sillas
print(aula_completa)

puntos_n1 = 48
puntos_n2 = 62
puntos_total = puntos_n1 + puntos_n2
juego_conseguido = puntos_total >= 100
print(juego_conseguido)

# Intercambiando valores.
juan = 200
maria = 15
temporal = juan
juan = maria
maria = temporal
print(juan)
print(maria)

juan, maria = 200, 15
juan, maria = maria, juan
print(juan)
print(maria)

# Tambien pueden almacenar cadenas de caracteres.
frase = "Esto es una frase"
print(frase)

# Concatenar cadenas de caracteres.
print("Hola, " + "que tal")

cadena1 = "Hola, "
cadena2 = "que tal"
print(cadena1 + cadena2)

nombre = "Luis "
apellido = "Merino"
print("Me llamo " + nombre + apellido)

nombre2 = "Juan"
apellido2 = "Perez"
print("Me llamo", nombre2, apellido2)

# Repetir cadenas de caracteres.
print("Hola " * 3)
cadena3 = "Hola "
print(cadena3 * 3)
