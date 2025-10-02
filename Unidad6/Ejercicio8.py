#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    IMC= peso / (altura**2)
    return IMC

peso=float(input("Por faovor, ingrese el peso en kilogramos: "))
altura=float(input("Por favor, ingrese su altura en metros: "))

resultado=calcular_imc(peso, altura)

print(f"Dado su peso de {peso} kilogramos y su altura de {altura} metros, el índice de masa corporal es {resultado:.2f}.")