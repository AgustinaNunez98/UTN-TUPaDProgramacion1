#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente

for i in range(100, 0, -1): # empieza en 100 y termina en 0, bajando de a uno
    if i % 2 == 0: # El operador % da el resto de la división, si el resto es igual a 0 es par.
        print(i) # Muestra por consola todos los números pares