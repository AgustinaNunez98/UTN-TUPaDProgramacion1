#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("Menú de opciones: \n1. Agregar productos \n0. Salir.")
opcion = int(input("Ingrese una opción: "))

with open("Unidad8/productos.txt", "r") as archivo:
    for linea in archivo:
        nombre,precio,cantidad=linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}.")

while opcion != 0:
    if opcion == 1:
            archivo = open("Unidad8/productos.txt", "a")
            nombre=input("Ingrese el nombre del nuevo producto: ")
            precio=float(input("Ingrese el precio del nuevo producto: "))
            cantidad=int(input("Ingrese la cantidad del nuevo producto: "))
            archivo.write(f"{nombre},{precio},{cantidad}\n")
            archivo.close()

    print("Menú de opciones: \n1. Agregar productos \n0. Salir.")
    opcion = int(input("Ingrese una opción: "))