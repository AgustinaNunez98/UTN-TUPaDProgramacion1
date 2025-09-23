#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

import random
list_random=[]
element_random=0
numbers_pairs=[]
numbers_impairs=[]

for i in range (15):
    element_random=random.randint(1, 100)
    list_random.append(element_random)
    if element_random % 2 == 0:
        numbers_pairs.append(element_random)
    else:
        numbers_impairs.append(element_random)
print(*list_random, sep=", ")
print(f"\nHay {len(numbers_pairs)} números pares y {len(numbers_impairs)} números impares")