# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"{precios_frutas} diccionario punto 1")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2000
print(f"{precios_frutas} diccionario punto 2")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#  desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
print(f"{precios_frutas.keys()} diccionario punto 3")

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
agenda_telefonica = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero_telefono = input(f"Ingresá el número de {nombre}: ")
    agenda_telefonica[nombre] = numero_telefono
consulta = input("Ingresá el nombre del contacto que querés buscar: ")
if consulta in agenda_telefonica:
    print(agenda_telefonica[consulta])
else:
    print("El contacto no existe en la agenda")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
frase_usuario = input("Ingrese una frase: ")
palabras = frase_usuario.split()
palabras_unicas = set(palabras)
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {frecuencia_palabras}")

# 6) Permití ingresar los nombres de 3 alumnos, 
# y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
# Crear diccionario vacío para guardar alumnos y sus notas
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}
ambos = parcial1.intersection(parcial2)
print("Aprobaron ambos parciales:", ambos)
solo_uno = parcial1.symmetric_difference(parcial2)
print("Aprobaron solo uno de los dos:", solo_uno)
al_menos_uno = parcial1.union(parcial2)
print("Aprobaron al menos un parcial:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
stock_productos = {
    "fideos": 100,
    "arroz": 47,
    "leche": 17,
    "sal": 0
}
producto = input("Ingresá el nombre de un producto para consultar su stock: ")
if producto in stock_productos:
    print(f"Quedan {stock_productos[producto]} unidades de {producto}")
    agregar = input("Queres agregar unidades a este producto? (s/n): ")
    if agregar == "s" or agregar == "S" :
        cantidad = int(input("Cuantas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades")
else:
    print(f"No tenemos stock del producto ingresado: {producto}")
    agregar_nuevo = input("Querés agregarlo al stock? (s/n): ")
    if agregar_nuevo == "s" or agregar_nuevo == "S":
        cantidad_nueva = int(input("Cuántas unidades querés ingresar?: "))
        stock_productos[producto] = cantidad_nueva

print(f"Stock actualizado: {stock_productos}")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
# Agenda con tuplas como clave: (día, hora)
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio"
}
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora: ")
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, 
# construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Perú": "Lima"
}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print(f"Diccionario invertido: {invertido} ")






