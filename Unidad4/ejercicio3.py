#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

contador=1
termina=100
suma=0

while contador < termina :
    suma = suma + contador
    contador += 1

print(f"La suma es {suma}")