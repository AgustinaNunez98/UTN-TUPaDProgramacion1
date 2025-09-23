#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

products=[]

for i in range (5):
    product= input("Por favor, ingrese un producto: ")
    products.append(product) #agrega un producto al final de la lista

print(*products, sep=", ")

remove_product=input("\nPor favor, ingrese el producto que desea eliminar: ")

if remove_product in products:
    products.remove(remove_product)
    print(f"\nSe elimino el {remove_product} correctamente.")
else:
    print(f"\nEl producto {remove_product} no se encuentra en la lista.")

products.sort() #ordena los elementos de la lista sin crear una lista nueva.
print(*products, sep=", ")