#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

import statistics

def calcular_promedio(a, b, c):
    promedio=statistics.mean([a, b, c])
    return promedio

num1=int(input("Por favor, ingrese el primer número: "))
num2=int(input("Por favor, ingrese el segundo número: "))
num3=int(input("Por favor, ingrese el tercer número: "))

resultado=calcular_promedio(num1, num2, num3)

print(f"\nEl promedio de {num1}, {num2} y {num3} es {resultado: .2f}.")