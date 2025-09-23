#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

notes=[
    [7, 8, 9],
    [8, 9, 8],
    [9, 10, 9],
    [4, 3, 2],
    [6, 8, 9],
]

avarege=0

for i in range (len(notes)):
    average= sum(notes[i])/len(notes[i])
    print(f'El promedio del alumno {i+1} su promedio es {average}')

subject=len(notes[0])
subject_average=0
for i in range(subject):
    suma= 0
    for j in range(len(notes)):
        suma = notes[j][i]
    subject_average= suma/subject
    subjects= i+1
    print(f"El promedio de la materia {i+1} es {subject_average}")

