#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos={}

for i in range(5):
    nombre=input("Ingrese el nombre del contacto nuevo: ")
    numero=input("Ingrese el numero del contacto: ")
    contactos.update({nombre: numero})

print(contactos)

consulta=input("Ingrese el nombre del contacto que desee ver: ")
if consulta in contactos:
    print(contactos[consulta])
else:
    print("El nombre ingresado no se encuentra entre los contactos.")