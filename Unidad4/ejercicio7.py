#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
sum_i=0

num=int(input("Ingrese un número entero positivo: "))
if num > 0 :
    for i in range (0, num +1):
        if i % 2 == 0 :
            sum_i= sum_i + i
    print(sum_i)
elif num < 0 :
    input("Debe ingresar un número positivo\nPor favor, vuelva a ingresar un número: ")