#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

num=int(input("Ingrese un número entero: "))
sum_num=0

while num != 0 :
    sum_num = sum_num + num
    num=int(input("Ingrese un número entero: "))

print(f"La suma es {sum_num}")