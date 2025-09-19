#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
statistics_mode = mode(numeros_aleatorios)
statistics_median = median(numeros_aleatorios)
statistics_mean = mean(numeros_aleatorios)

if statistics_mean > statistics_median and statistics_median < statistics_mode : 
    print(f"Sesgo positivo o a la derecha. La mediana es {statistics_median}, la media es {statistics_mean} y la moda es {statistics_mode}.")
elif statistics_mean < statistics_median and statistics_median < statistics_mode :
    print(f"Sesgo negativo o a la izquierda. La mediana es {statistics_median}, la media es {statistics_mean} y la moda es {statistics_mode}.")
elif statistics_mode == statistics_mean == statistics_median :
    print(f"Sin sesgo. La mediana es {statistics_median}, la media es {statistics_mean} y la moda es {statistics_mode}.")
