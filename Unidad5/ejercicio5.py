#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

students=[]

for i in range (2):
    student=input("Por favor, ingrese el nombre del alumno presente: ")
    students.append(student)

print(*students, sep=", ")

option=input('\nPor favor, indicar la opción deseada: \nA. Si desea agregar un nuevo estudiante.\nB. Si desea eliminar un estudiante existente.\n').lower()

if option == "a":
    student=input('Por favor, ingrese el nombre del alumno que desea agregar: ')
    students.append(student)
    print(f'Se agrego correctamento el alumno {student}')
elif option == "b":
    student=input('Por favor, ingrese el nombre del alumno que desea eliminar.')
    if student in students:
        students.remove(student)
        print(f'Se elimino el alumno {student} correctamente.')
    else:
        print(f'El alumno {student} no se encuentra en la lista.')