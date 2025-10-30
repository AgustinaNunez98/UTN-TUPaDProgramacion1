#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error.

buscado = input("Ingrese el nombre del producto a buscar: ")

producto_encontrado = False
with open("Unidad8/productos.txt", "r") as archivo:
    for linea in archivo:
        nombre,precio,cantidad=linea.strip().split(",")
        if "nombre".lower() == buscado.lower():
            print(f"Producto encontrado:\nNombre: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
            encontrado = True
            break

if not producto_encontrado:
    print("Error: Producto no encontrado.")