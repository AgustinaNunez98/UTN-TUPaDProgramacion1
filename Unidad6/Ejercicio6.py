#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1, 11):
        resultado= numero * i
        print(f"{numero} x {i} = {resultado}")

numero=int(input("Por favor, ingrese un número: "))
tabla_multiplicar(numero)