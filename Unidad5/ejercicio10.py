#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

sales = [
    [5, 8, 6, 4, 7, 3, 2],  
    [3, 6, 2, 8, 4, 9, 1],   
    [7, 2, 5, 3, 6, 4, 8],   
    [4, 3, 7, 9, 5, 2, 6]    
]

print("Totales por producto:")
for product in range(4): 
    full = 0
    for day in range(7): 
        full += sales[product][day]
    print(f"Producto {product}: {full}")

mayor_day = 0
sum_mayor = 0
for dia in range(7): 
    sum_day = 0
    for producto in range(4): 
        sum_day += sales[product][day]
    if sum_day > sum_mayor:
        sum_mayor = sum_day
        mayor_day = day

print(f"El día con más ventas fue el día {mayor_day} con {sum_mayor} ventas.")

product_more = 0
sales_more = 0
for product in range(4):
    full = 0
    for day in range(7):
        full += sales[product][day]
    if full > sales_more:
        sales_more = full
        product_more = product

print(f"El producto más vendido fue el producto {product_more} con {sales_more} ventas.")
