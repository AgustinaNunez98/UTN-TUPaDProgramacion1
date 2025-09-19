# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
saludo = "Hola Mundo!"
print(saludo)

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_residencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = input("Ingrese el radio del círculo, por favor: ")
area = 3.14159 * float(radio) ** 2
perimetro = 2 * 3.14159 * float(radio)
print (f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600    
print(f"{segundos} segundos equivalen a {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
tablas = [numero * i for i in range(1, 100)]
for i, resultado in enumerate(tablas, start=1):
    print(f"{numero} x {i} = {resultado}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese el primer número entero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0: "))
Suma = num1 + num2
Resta = num1 - num2
Multiplicacion = num1 * num2
Division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"
print(f"Resultados:\nSuma: {Suma}\nResta: {Resta}\nMultiplicación: {Multiplicacion}\nDivisión: {Division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
altura = float(input("Ingrese su altura en metros (por ejemplo, 1.75): "))
peso = float(input("Ingrese su peso en kilogramos (por ejemplo, 70): "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números {num1}, {num2} y {num3} es: {promedio:.2f}")