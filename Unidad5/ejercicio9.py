#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tateti=[
    [ "-", "-", "-"],
    [ "-", "-", "-"],
    [ "-", "-", "-"]
]

turnos = 0

while turnos < 9:
   
    for fila in tateti:
        print(fila)
    print()

    if turnos % 2 == 0:
        jugador_num = 1
        ficha = "X"
    else:
        jugador_num = 2
        ficha = "O"

    row = int(input(f"Jugador {jugador_num} ({ficha}), fila (0-2): "))
    column = int(input(f"Jugador {jugador_num} ({ficha}), columna (0-2): "))

   
    if tateti[row][column] == "-":
        tateti[row][column] = ficha
        turnos += 1
    else:
        print("¡Casilla ocupada! Elegí otra.")

for fila in tateti:
    print(fila)
