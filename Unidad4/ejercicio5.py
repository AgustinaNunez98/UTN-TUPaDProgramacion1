#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_entero=random.randint(0, 9)

num=int(input("Adivine el número: "))
sum_intentos=0

while num != num_entero :
    sum_intentos += 1
    num=int(input("Número incorrecto.\nVuelva a intentarlo: "))

print(f"Felicitaciones! A ganado el juego!\nIntentos: {sum_intentos}")