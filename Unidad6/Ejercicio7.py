#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma= a + b
    resta= a - b
    multiplicar= a * b
    if b != 0:
        dividir= a / b
    else:
        dividir="No se puede dividir por cero."

    return (suma, resta, multiplicar, dividir)

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

resultados= operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")