# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos 
# los números enteros entre 1 y el número que indique el usuario
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
def factoriales_n(num):
    for i in range(1, num+1):
        print(factorial(i))
# Programa principal
numero_usuario_1 = int(input("Ingrese un número para calcular los factoriales desde 1 hasta el número ingresado: "))
factoriales_n(numero_usuario_1)

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)
def mostrar_serie(num):
    for i in range(num + 1):
        print(fibonacci(i), end=", ")
# Programa principal
numero_usuario_2 = int(input("Ingresa la posición del algoritmo de fibonacci que desea saber y le mostraremos la serie hasta esa posicion "))
mostrar_serie(numero_usuario_2)
print("")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
# Programa principal
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado_3 = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado_3}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2.
#  Para convertir un número decimal a binario, se puede seguir este procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
def evaluar_binario(num):
    if num == 0:
        print("El número binario es: 0")
    else:
        binario = decimal_a_binario(num)
        print(f"El número binario es: {binario}")
# Programa principal
numero_binario = int(input("Ingrese un número entero positivo: "))
evaluar_binario(numero_binario)

# 5) Implementá una función recursiva llamada es_palindromo(palabra) 
# que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed(). 
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
def evaluar_palindromo(palabra):
    if es_palindromo(palabra):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
# Programa principal
palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
evaluar_palindromo(palabra)

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) 
# que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
# Programa principal
numero_usuario_6 = int(input("Ingrese un número entero positivo: "))
resultado_6 = suma_digitos(numero_usuario_6)
print(f"La suma de los dígitos de {numero_usuario_6} es: {resultado_6}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
# Programa principal
nivel_inferior = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
total_bloques = contar_bloques(nivel_inferior)
print(f"Total de bloques necesarios para construir la pirámide: {total_bloques}")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if numero % 10 == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)
def evaluar_conteo(numero, digito):
    if 0 <= digito <= 9:
        resultado = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
    else:
        print("El dígito ingresado no es válido. Debe estar entre 0 y 9.")
# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar (0 a 9): "))
evaluar_conteo(numero, digito)


