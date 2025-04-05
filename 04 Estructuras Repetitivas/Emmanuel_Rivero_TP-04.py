import random
# 1) Crea un programa que imprima en pantalla todos los números enteros 
# desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(1, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero_usuario = int(input("Ingrese un número entero: "))
contadorDigitos = 0
while numero_usuario > 0:
    numero_usuario //= 10
    contadorDigitos += 1
print(f"El número seleccionado tiene {contadorDigitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, 
# excluyendo esos dos valores.
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
inicio = min(primer_numero, segundo_numero) + 1
fin = max(primer_numero, segundo_numero)
suma = 0
for i in range(inicio, fin):
    suma += i
print(f"La suma de los numeros comprendidos entre ambos ingresados es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero_usuario_4 = int(input("Ingrese un número entero (0 para finalizar): "))
suma_secuencial = 0
while numero_usuario_4 != 0:
    suma_secuencial += numero_usuario_4
    numero_usuario_4 = int(input("Ingrese otro número entero (0 para finalizar): "))
print(f"La suma total de los números ingresados es: {suma_secuencial}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
numero_a_adivinar = random.randint(0, 9)
numero_usuario_5 = int(input("Ingrese un número entero del 0 al 9 para tratar de adivinar: "))
cantidad_intentos = 1
while numero_a_adivinar != numero_usuario_5:
    numero_usuario_5 = int(input("Vuelva a ingresar otro número para tratar de adivinar: " ))
    cantidad_intentos += 1
print(f"Usted adivinó el número luego de {cantidad_intentos} intentos")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero_usuario_7 = int(input("Ingrese un número entero: "))
suma_enteros = 0
for i in range(numero_usuario_7):
    suma_enteros += i
print(f"La suma de todos los números comprendidos entre 0 y el número ingresado es {suma_enteros}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
numero_usuario_8 = 0
numero_intentos = 100
cantidad_positivos = 0
cantidad_negativos = 0
cantidad_pares = 0
cantidad_impares = 0
for i in range(numero_intentos):
    numero_usuario_8 = int(input("Ingrese un número: "))
    if numero_usuario_8 > 0:
        cantidad_positivos += 1
    elif numero_usuario_8 < 0:
        cantidad_negativos += 1
    if numero_usuario_8 % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
print(f"La cantidad de números positivos ingresados es {cantidad_positivos}, de negativos es {cantidad_negativos}, de pares es {cantidad_pares}, y de números impares es {cantidad_impares}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
numero_intentos_9 = 100
total_acumulado = 0
media = 0
numero_usuario_9 = 0
for i in range(numero_intentos_9):
    numero_usuario_9 = int(input("Ingrese un número: "))
    total_acumulado += numero_usuario_9
media = total_acumulado / numero_intentos_9
print(f"La media de los números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero_usuario_10 = int(input("Ingrese un número entero: "))
digito_a_guardar = 0
numero_invertido = 0
while numero_usuario_10 > 0:
    digito_a_guardar = numero_usuario_10 % 10
    numero_invertido = numero_invertido * 10 + digito_a_guardar
    numero_usuario_10 //= 10
print(f"El número que ingreso invertido es: {numero_invertido}")
