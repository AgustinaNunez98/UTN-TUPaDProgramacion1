#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).

list=[1, 2, 3, 4, 5, 6, 7]
last_number=list[-1]
print(f'La lista original es:')
print(*list)
print('La lista nueva es: ')
print(last_number,*list[:6])