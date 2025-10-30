#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

from collections import Counter

frase = input("Ingrese una frase: ")

palabras_unicas = set(frase.split())

contador = Counter(frase.split())

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", contador)

