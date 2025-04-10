from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota_usuario = int(input("Ingrese su nota: "))
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero_par = int(input("Ingrese un número: "))
if numero_par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
categoria_edad = int(input("Ingrese su edad: "))
if categoria_edad < 12:
    print("Usted es un Niño/a")
elif categoria_edad >= 12 and categoria_edad < 18:
    print("Usted es un Adolescente")
elif categoria_edad >= 18 and categoria_edad < 30:
    print("Usted es un Adulto/a joven")
else:
    print("Usted es un Adulto/a mayor")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contrasenia_usuario = input("Ingrese su contraseña: ")
if len(contrasenia_usuario) >= 8 and len(contrasenia_usuario) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
# Imprimir el resultado por pantalla.
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == moda and media == mediana and moda == mediana:
    print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase_usuario = input("Ingrese una frase o palabra: ")
ultima_letra = frase_usuario[-1]
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase_usuario}!")
else:
    print(frase_usuario)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario 
# e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas
nombre_usuario_8 = input("Ingrese su nombre: ")
numero_a_evaluar = int(input("Ingrese la opcion que desee: 1 para convertir su nombre a mayusculas. 2 para convertir su nombre a minusculas, o 3 para agregar la mayuscula solo a la primer letra: "))
if numero_a_evaluar == 1:
    print(nombre_usuario_8.upper())
elif numero_a_evaluar == 2:
    print(nombre_usuario_8.lower())
elif numero_a_evaluar == 3:
    print(nombre_usuario_8.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir 
# por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio_usuario = input("Ingrese en que hemisferio se encuentra: N para norte y S para sur: ").upper()
mes = int(input("Ingrese el numero de mes en el que se encuentra: "))
dia = int(input("Ingrese el dia en el que se encuentra: "))
fecha = (mes, dia)
if fecha >= (12, 21) or fecha <= (3, 20):
    if hemisferio_usuario == "N":
        print("Estas en Invierno")
    else:
        print("Estas en Verano")
elif fecha >= (3, 21) and fecha <= (6, 20):
    if hemisferio_usuario == "N":
        print("Estas en Primavera")
    else:
        print("Estas en Otoño")
elif fecha >= (6, 21) and fecha <= (9, 20):
    if hemisferio_usuario == "N":
        print("Estas en Verano")
    else:
        print("Estas en Invierno")
elif fecha >= (9, 21) and fecha <= (12, 20):
    if hemisferio_usuario == "N":
        print("Estas en Otoño")
    else:
        print("Estas en Primavera")


