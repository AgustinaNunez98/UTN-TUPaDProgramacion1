#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

quantity_entered=0
quantity_pairs=0
quantity_odd_number=0
quantity_negative=0
quantity_positive=0

while quantity_entered < 100 :
    number=int(input("Por favor ingrese un número: "))
    quantity_entered += 1
    if number % 2 == 0 :
        quantity_pairs +=1
    elif number % 2 !=0 :
        quantity_odd_number +=1
    elif number > 0 :
        quantity_positive +=1
    elif number < 0 :
        quantity_negative +=1

print(f"{quantity_pairs} de los números son pares.\n{quantity_odd_number} de los números son impares.\n{quantity_positive} de los números son positivos.\n{quantity_negative} de los números son negativos.")