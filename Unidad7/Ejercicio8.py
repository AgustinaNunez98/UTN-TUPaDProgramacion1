#) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

# Crear el diccionario inicial
productos = {"azucar": 10, "yerba": 5, "cafe": 8}
producto = input("Ingrese el nombre del producto: ").lower()

if producto in productos:
    print(f"El stock actual de {producto} es {productos[producto]} unidades.")
    agregar = int(input("¿Desea agregar más unidades? "))
    productos[producto] += agregar
    print(f"Stock actualizado de {producto}: {productos[producto]} unidades.")
else:
    print(f"El producto '{producto}' no existe.")
    consulta=input("Desea agregar un producto nuevo?").lower()
    if consulta == "si":
        nuevo_stock = int(input("Ingrese el stock inicial de este nuevo producto: "))
        productos[producto] = nuevo_stock
        print(f"Producto '{producto}' agregado con {nuevo_stock} unidades.")
    else:
        print("\nDiccionario actualizado de productos y stock:")
print(productos)
print("Muchas gracias por consultar el diccionario de stock")