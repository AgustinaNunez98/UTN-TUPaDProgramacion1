#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

agregar = input("¿Desea agregar un nuevo producto? (si/no): ").lower()
while agregar == "si":
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    agregar = input("¿Desea agregar otro producto? (si/no): ").lower()

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo productos.txt actualizado.")