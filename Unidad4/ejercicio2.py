#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

num=int(input("Por favor, ingrese un número: ")) #se utiliza float para que el usuario pueda ingresar un número entero o con decimales.

cadena_num=str(num)
longitud_num=len(cadena_num)

while num != float :
 print(f"El número ingresado {num}, contiene {longitud_num} de dígitos.")
 break