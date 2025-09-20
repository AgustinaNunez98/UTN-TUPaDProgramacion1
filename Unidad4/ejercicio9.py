#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

sum_numer=0

for i in range (100) : 
    number=int(input("Por favor ingrese un número: "))
    sum_numer = sum_numer + number
media=sum_numer/100
print(f"La media es {media}.")