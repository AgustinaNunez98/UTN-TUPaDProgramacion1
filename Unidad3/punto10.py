#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año:                                                 #Estación en el hemisferio norte:             #Estación en el hemisferio sur:             
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)                   Invierno                                       Verano
#Desde el 21 de marzo hasta el 20 de junio (incluidos)                       Primavera                                       Otoño
#Desde el 21 de junio hasta el 20 de septiembre (incluidos)                    Verano                                      Invierno
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)                Otoño                                       Primavera

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio=input("Por favor ingrese en cuál hemisferio se encuentra: ")
hemisferio_minuscula= hemisferio.lower()


if hemisferio_minuscula == "norte":
    mes=int(input("Ingrese que mes es, en número: "))
    dia=int(input("Ingrese el día de hoy: "))
    if dia >= 21 and dia < 20 and mes == 12 or mes <= 3 :
        print("Es invierno")
    elif dia >= 21 and dia < 20 and mes == 3 or mes <= 6 :
        print("Es Primavera")
    elif dia >= 21 and dia < 20 and mes == 6 or mes <= 9 :
        print("Es Verano")
    elif dia >= 21 and dia < 20 and mes == 9 or mes <= 12 :
        print("Es Otoño")
elif hemisferio_minuscula == "sur":
    mes=int(input("Ingrese que mes es, en número: "))
    dia=int(input("Ingrese el día de hoy: "))
    if dia >= 21 and dia < 20 and mes == 12 or mes <= 3 :
        print("Es Verano")
    elif dia >= 21 and dia < 20 and mes == 3 or mes <= 6 :
        print("Otoño")
    elif dia >= 21 and dia < 20 and mes == 6 or mes <= 9 :
        print("Es invierno")
    elif dia >= 21 and dia < 20 and mes == 9 or mes <= 12 :
        print("Es Primavera")