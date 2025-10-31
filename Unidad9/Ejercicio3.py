#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula n^m = n∗n(m−1)
#. Prueba esta función en un 
#algoritmo general
num1=int(input("Ingrese exponente: "))
num2=int(input("Ingrese base: "))
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia (base, exponente-1)

print(f"{num2} elevado a {num1} es {potencia(num2,num1)}")