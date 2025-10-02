#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit= (celsius * 9/5) + 32
    return fahrenheit

celsius= int(input("Ingrese la temperatura en grados Celsius: "))
resultado=celsius_a_fahrenheit(celsius)

print(f"La temperatura en fahrenheit es {resultado: .2f}.")