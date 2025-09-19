#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

cadena = input("Ingrese una frase o palabra: ")
ultimo_caracter = cadena[-1]
vocales = "aeiou"
if ultimo_caracter.lower() in vocales :
    print(f"{cadena}!")
else :
 print(cadena)