#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

while True :
 print ("Menú de opciones\n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. \n0. Salir")
 opcion = int(input("Selecciono la opción: "))

 if opcion == 1 :
    nombre_con_mayuscula = nombre.upper()
    print (nombre_con_mayuscula)
 elif opcion == 2 :
    nombre_en_minuscula = nombre.lower()
    print(nombre_en_minuscula)
 elif opcion == 3 :
    primer_letra_en_mayuscula = nombre.title()
    print(primer_letra_en_mayuscula)
 elif opcion == 0 :
    print("Selecciono salir.")
    break
 else :
    print("Opción no valida. Vuelva a elegir una opción, por favor.")