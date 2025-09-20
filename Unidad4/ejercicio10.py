#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

number=int(input("Por favor ingrese un número: "))
number_string=str(number)
string_invested=number_string[::-1]

while number < 0 :
    int(input("Debe ingresar un número positivo: "))

print(f"El nûmero ingresado es {number} e invertido es {string_invested}")