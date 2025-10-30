#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1={1, 2, 3, 4, 5}
parcial2={4, 5, 6, 7}

ambos = parcial1.intersection(parcial2)
solo_uno = parcial1.symmetric_difference(parcial2)
al_menos_uno = parcial1.union(parcial2)

print("\nAlumnos que aprobaron ambos parciales:", ambos)
print("Alumnos que aprobaron solo uno de los dos parciales:", solo_uno)
print("Alumnos que aprobaron al menos un parcial:", al_menos_uno)