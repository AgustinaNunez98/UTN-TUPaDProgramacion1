#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notes=[7, 8, 9, 10, 9, 8, 6 , 5, 2, 10]
quantity_notes=len(notes)
sum=sum(notes) #Suma todos los elementos de la lista
average=0
notes_organized=sorted(notes) #ordena los elementos de la lista, de menos a mayor.
min=min(notes) #busca el elemento minimo de la lista
max=max(notes) #busa el elemento maximo de la lista

for i in range (len(notes_organized)):
    if i == len(notes_organized)-1:
        print(notes_organized[i]) #al último elemento no se le agrega una coma
    else:
        print(notes_organized[i], end= ", " ) #al final de cada elemento se agrega una coma 
    average=sum/quantity_notes

print(f"\nEl promedio de las {quantity_notes} notas es {average}.")
print(f"\nLa nota más alta es  {max} y la nota más baja es {min}.")
