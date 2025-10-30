#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

original = {"Brasil": "Brasilia", "Ecuador": "Quito"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)