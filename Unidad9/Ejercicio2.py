#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique.
num=int(input("Ingrese un número para calcular la serie de fibonacci: "))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print("Serie de fibonacci ")
for i in range(num):
    print(fibonacci(i),end=" ")

print()