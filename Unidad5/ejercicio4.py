#4) Dada una lista con valores repetidos:
#data=[1, 3, 5, 3, 7, 1, 9, 5, 3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

data=[1, 3, 5, 3, 7, 1, 9, 5, 3]
data_organized=[]

for i in data:
    if i not in data_organized:
        data_organized.append(i)


data_organized.sort() #ordena los elementos de la lista sin crear una lista nueva.
print(*data)
print(*data_organized, sep=", ")