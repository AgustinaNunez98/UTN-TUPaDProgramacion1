#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos= {}

for i in range (3):
    nombre=input("Ingrese el nombre del alumnos: ")
    notas=[]
    for j in range (3):
        nota=int(input("Ingrese la nota: "))
        notas.append(nota)
    notas=tuple(notas)
    alumnos[nombre]=notas

for nombre, notas in alumnos.items():
    promedio= sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio}.")