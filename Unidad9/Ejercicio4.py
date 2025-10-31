#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto.

def a_binario(n):
    if n == 0:
        return " "
    else:
        return a_binario(n//2)+str(n%2)

num=int(input("Ingrese el número que desea convertir en binario: "))
print(f"El {num}, en binario es {a_binario(num)}")