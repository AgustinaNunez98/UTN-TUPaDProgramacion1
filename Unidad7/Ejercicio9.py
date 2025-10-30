#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda={("Jueves", "11:30"): "Dentista", ("Viernes", "8:00"): "Entreno acrobacia en tela"}

dia=input("Ingrese el día: ").title()
hora=input("Ingrese la hora (eje: 10:00): ")
consulta= (dia, hora)

if consulta in agenda:
    print(f"El {dia} a las {hora} hay: {agenda[consulta]}")
else:
    print(f"No hay actividades programadas para {dia} a las {hora}.")