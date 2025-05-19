import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")
# Programa principal
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
# Programa principal
nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# Programa principal
nombre_usuario_3 = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su residenncia: ")
informacion_personal(nombre_usuario_3, apellido_usuario, edad_usuario, residencia_usuario)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
# Programa principal
radio = int(input("Ingrese el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area es: {area} y el perímetro es: {perimetro}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600
# Programa principal
segundos = int(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"Las horas respectivas a los segundos ingresados son: {horas}")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
# y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
# Programa principal
numero_usuario_6 = int(input("Ingrese un número para construir su tabla: "))
tabla_multiplicar(numero_usuario_6)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)
# Programa principal
primer_numero = int(input("Ingrese el primer nnúmero: "))
segundo_numero = int(input("Ingrese el segunndo nnúmero: "))
resultado = operaciones_basicas(primer_numero, segundo_numero)
print(f"La suma de los números es: {resultado[0]}")
print(f"La resta de los números es: {resultado[1]}")
print(f"La multiplicación de los números es:: {resultado[2]}")
print(f"La división de los números es:: {resultado[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos 
# y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
# Programa principal
peso_usuario = float(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso_usuario, altura_usuario)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura 
# en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Programa principal
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit}°F")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
# Programa principal
primer_numero_10 = int(input("Ingrese el primer número: "))
segundo_numero_10 = int(input("Ingrese el segundo número: "))
tercer_numero_10 = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(primer_numero_10, segundo_numero_10, tercer_numero_10)
print(f"El promedio de los tres números ingresados es: {promedio}")
