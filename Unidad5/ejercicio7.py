#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

matriz=[
    [30, 10],
    [28, 13],
    [29, 12],
    [26, 9],
    [25, 7],
    [27, 8],
    [32, 10]
    ]

mintemperature=0
maxtemperature=0

for i in matriz:
    mintemperature += i[1]
    maxtemperature += i[0]

mintemperature= mintemperature/7
maxtemperature= maxtemperature/7
maxi=0
print(f'La temperatura promedio de la minima es {int(mintemperature)} y la maxima es {int(maxtemperature)}')
maxi=max(matriz[0])
print(f'La el día con mayor amplitud fue el día con {maxi} de maxima')