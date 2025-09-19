# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

numero=float(input("Ingrese la magnitud del terremoto: "))

if numero < 3 :
    print("Muy leve.\nImperceptible")
elif numero >= 3 and numero < 4 :
    print("Leve.\nLigeramente perceptible.")
elif numero >= 4 and numero < 5 :
    print("Moderado.\nSentido por personas, pero generalmente no causa daño.")
elif numero >= 5 and numero < 6 :
    print("Fuerte.\nPuede causar daños en estructuras débiles.")
elif numero >= 6 and numero < 7 :
    print("Muy fuerte.\nPuede causar daños significativos.")
elif numero >= 7 :
    print("Extremo.\nPuede causar graves daños a gran escala.")