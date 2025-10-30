#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
#os.path.exists(productos.txt)

with open("Unidad8/productos.txt", "r") as archivo:
    for linea in archivo:
        nombre,precio,cantidad=linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}.")