import statistics
import os

def cargar_paises(archivo_paises):  # lee el archivo y muestra por pantalla la lista de países
    paises = []

    with open(archivo_paises, "a+") as archivo:
        archivo.seek(0)  # el programa lee o escribe desde el principio de nuevo
        lineas = archivo.readlines()  # lee todas las lineas del archivo y los almacena en la lista lineas

        if len(lineas) == 0:
            print(f"El archivo {archivo_paises} esta vacio.")
            return paises
        else:
            for linea in lineas[1:]:  # leemos todas las lineas menos el encabezado
                linea = linea.strip()  # saca los espacios al principio y saltos de línea
                partes = linea.split(",")

                if len(partes) == 4:  # verificamos que tenga 4 columnas
                    nombre = partes[0]
                    poblacion = partes[1]
                    superficie = partes[2]
                    continente = partes[3]

                    if poblacion.isdigit() and superficie.isdigit():  # validamos que poblacion y superficie sean números enteros
                        poblacion = int(poblacion)
                        superficie = int(superficie)
                        paises.append([nombre, poblacion, superficie, continente])
                    else:
                        print("Error en los datos numericos, se omite: ",linea)
                else:
                    print("Línea con formato incorrecto, se omite: ", linea)
        return paises

def mostrar_paises(lista_paises):
    print("\n   Lista de países\n")
    if len(lista_paises) == 0:
        print("\nNo hay países cargados para mostrar.")
    else:
        for pais in lista_paises:
            nombre = pais[0]
            poblacion = pais[1]
            superficie = pais[2]
            continente = pais[3]

            print(f"Nombre: {nombre}")
            print(f"Población: {poblacion}")
            print(f"Superficie: {superficie} km²")
            print(f"Continente: {continente}\n")

def agregar_pais(archivo_paises):
    print("\n Agregar nuevo país ")
    nombre = input("Ingrese el nombre del país: ").strip().title()
    poblacion = input("Ingrese la población: ").strip()
    superficie = input("Ingrese la superficie: ").strip()
    continente = input("Ingrese el continente: ").strip().title()

    if nombre != "" and poblacion != "" and superficie != "" and continente != "": 
        if poblacion.isdigit() and superficie.isdigit():    
            poblacion = int(poblacion)
            superficie = int(superficie)

            with open(archivo_paises, "r") as archivo:
                lineas = archivo.readlines()
            if len(lineas) > 0 and not lineas[-1].endswith("\n"):   # Verificamos si el último carácter del archivo es salto de línea
                salto = "\n"
            else:
                salto = ""
            with open(archivo_paises, "a") as archivo:  # Ahora abrimos en modo append y escribimos correctamente
                archivo.write(f"{salto}{nombre},{poblacion},{superficie},{continente}\n")

            print(f"\nPaís '{nombre}' agregado correctamente al archivo.")
        else:
            print("Población y superficie deben ser números enteros positivos.")
    else:
        print("Todos los campos deben estar completos.")

def actualizar_pais(archivo_paises, lista_paises):
    print("\n Actualizar datos de un país ")

    nombre_buscado = input("Ingrese parte del nombre del país a actualizar: ").strip().title()
    coincidencias = []
    pais_a_modificar = []
    hay_opcion_valida = 0

    for pais in lista_paises:   # Buscar coincidencias parciales
        if nombre_buscado in pais[0]:
            coincidencias.append(pais)

    if len(coincidencias) == 0:
        print("No se encontró ningún país con ese nombre o coincidencia.")
    else:
        if len(coincidencias) > 1:
            print("\nSe encontraron varios países:")
            indice = 1
            for p in coincidencias:
                print(f"{indice}. {p[0]}")
                indice = indice + 1

            opcion = input("Seleccione el número del país a actualizar: ").strip()

            if opcion.isdigit():
                opcion = int(opcion)
                if opcion > 0 and opcion <= len(coincidencias):
                    pais_a_modificar = coincidencias[opcion - 1]
                    hay_opcion_valida = 1
                else:
                    print("Opción inválida.")
            else:
                print("Debe ingresar un número.")
        else:
            pais_a_modificar = coincidencias[0]
            hay_opcion_valida = 1


        if hay_opcion_valida == 1:  # Si se eligió un país válido
            print(f"\nPaís encontrado: {pais_a_modificar[0]}")
            print(f"Población actual: {pais_a_modificar[1]}")
            print(f"Superficie actual: {pais_a_modificar[2]} km²")

            print("\n¿Qué desea actualizar?")
            print("1. Solo la población")
            print("2. Solo la superficie")
            print("3. Ambas")

            opcion_cambio = input("Seleccione una opción: ").strip()
            cambio_realizado = 0

            if opcion_cambio == "1":
                nueva_poblacion = input("Nueva población: ").strip()
                if nueva_poblacion.isdigit():
                    pais_a_modificar[1] = int(nueva_poblacion)
                    print(f"Población actualizada para {pais_a_modificar[0]}")
                    cambio_realizado = 1
                else:
                    print("La población debe ser un número entero.")

            elif opcion_cambio == "2":
                nueva_superficie = input("Nueva superficie: ").strip()
                if nueva_superficie.isdigit():
                    pais_a_modificar[2] = int(nueva_superficie)
                    print(f"Superficie actualizada para {pais_a_modificar[0]}")
                    cambio_realizado = 1
                else:
                    print("La superficie debe ser un número entero.")

            elif opcion_cambio == "3":
                nueva_poblacion = input("Nueva población: ").strip()
                nueva_superficie = input("Nueva superficie: ").strip()
                if nueva_poblacion.isdigit() and nueva_superficie.isdigit():
                    pais_a_modificar[1] = int(nueva_poblacion)
                    pais_a_modificar[2] = int(nueva_superficie)
                    print(f"\nPoblación y superficie actualizadas para {pais_a_modificar[0]}")
                    cambio_realizado = 1
                else:
                    print("Ambos valores deben ser números enteros.")
            else:
                print("Opción inválida. No se realizaron cambios.")

            if cambio_realizado == 1:   # Guardar cambios si se realizó alguno
                with open(archivo_paises, "w") as archivo:
                    archivo.write("Nombre,Poblacion,Superficie,Continente\n")
                    for p in lista_paises:
                        archivo.write(f"{p[0]},{p[1]},{p[2]},{p[3]}\n")

                print("\nEl archivo fue actualizado correctamente.")

def buscar_pais(lista_paises):
    nombre_buscado = input("Ingrese el nombre del país a buscar: ").strip().lower()
    cantidad_encontrados = 0
    print("\n Resultados de la busqueda: ")

    for pais in lista_paises:
        if nombre_buscado in pais[0].lower():
            print("\n País encontrado ")
            print(f"Nombre: {pais[0]}")
            print(f"Población: {pais[1]}")
            print(f"Superficie: {pais[2]} km²")
            print(f"Continente: {pais[3]}")
            cantidad_encontrados = cantidad_encontrados + 1

    if cantidad_encontrados == 0:
        print("No se encontró ningún país que coincida con el texto ingresado.")

import statistics

def mostrar_estadisticas(lista_paises):
    print("\nEstadísticas de países: \n")

    if len(lista_paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
    else:
        poblaciones = [pais[1] for pais in lista_paises]
        superficies = [pais[2] for pais in lista_paises]

        mayor_poblacion = max(poblaciones)
        menor_poblacion = min(poblaciones)
        pais_mayor_poblacion = lista_paises[poblaciones.index(mayor_poblacion)][0]
        pais_menor_poblacion = lista_paises[poblaciones.index(menor_poblacion)][0]

        mayor_superficie = max(superficies)
        pais_mayor_superficie = lista_paises[superficies.index(mayor_superficie)][0]

        promedio_poblacion = statistics.mean(poblaciones)
        promedio_superficie = statistics.mean(superficies)

        print(f"País con mayor población: {pais_mayor_poblacion} - {mayor_poblacion}")
        print(f"País con menor población: {pais_menor_poblacion} - {menor_poblacion}")
        print(f"País con mayor superficie: {pais_mayor_superficie} - {mayor_superficie} km²")
        print(f"Población promedio: {promedio_poblacion:.0f}")
        print(f"Superficie promedio: {promedio_superficie:.0f}")

        print("\nCantidad de países por continente: \n")
        continentes = {}
        for pais in lista_paises:
            continente = pais[3]
            if continente in continentes:
                continentes[continente] = continentes[continente] + 1
            else:
                continentes[continente] = 1

        for cont, cantidad in continentes.items():
            print(f"{cont}: {cantidad} países")

def filtrar_por_continente(lista_paises):
    continente_buscado = input("Ingrese el nombre del continente: ").strip().lower()
    encontrados = 0

    print(f"\n Países de {continente_buscado.capitalize()}: \n")

    for pais in lista_paises:
        continente = pais[3].lower()
        if continente == continente_buscado:
            print(f"Nombre: {pais[0]}")
            print(f"Población: {pais[1]}")
            print(f"Superficie: {pais[2]} km²\n")
            encontrados = encontrados + 1

    if encontrados == 0:
        print("No se encontraron países en ese continente.")

def filtrar_por_poblacion(lista_paises):
    print("\n Filtrar países por rango de población ")

    minimo = input("Ingrese la población mínima: ").strip()
    maximo = input("Ingrese la población máxima: ").strip()

    if minimo.isdigit() and maximo.isdigit():
        minimo = int(minimo)
        maximo = int(maximo)

        if minimo > maximo:
            print("El valor mínimo no puede ser mayor que el máximo.")
        else:
            encontrados = 0
            print(f"\n Países con población entre {minimo} y {maximo}: \n")

            for pais in lista_paises:
                poblacion = pais[1]
                if poblacion >= minimo and poblacion <= maximo:
                    print(f"Nombre: {pais[0]}")
                    print(f"Población: {pais[1]}")
                    print(f"Superficie: {pais[2]} km²")
                    print(f"Continente: {pais[3]} \n")
                    encontrados = encontrados + 1

            if encontrados == 0:
                print("No se encontraron países dentro de ese rango.")
    else:
        print("Debe ingresar solo números enteros.")

def filtrar_por_superficie(lista_paises):
    print("\n Filtrar países por rango de superficie\n")

    minimo = input("Ingrese la superficie mínima km²: ").strip()
    maximo = input("Ingrese la superficie máxima km²: ").strip()

    if minimo.isdigit() and maximo.isdigit():
        minimo = int(minimo)
        maximo = int(maximo)

        if minimo > maximo:
            print("El valor mínimo no puede ser mayor que el máximo.")
        else:
            encontrados = 0
            print(f"\n Países con superficie entre {minimo} y {maximo} km²\n")

            for pais in lista_paises:
                superficie = pais[2]
                if superficie >= minimo and superficie <= maximo:
                    print(f"Nombre: {pais[0]}")
                    print(f"Población: {pais[1]}")
                    print(f"Superficie: {pais[2]} km²")
                    print(f"Continente: {pais[3]}\n")
                    encontrados = encontrados + 1

            if encontrados == 0:
                print("No se encontraron países dentro de ese rango.")
    else:
        print("Debe ingresar solo números enteros.")

def ordenar_paises(lista_paises):
    print("\n Ordenar países")
    print("1. Por nombre (A-Z)")
    print("2. Por población ascendente")
    print("3. Por población descendente")
    print("4. Por superficie ascendente")
    print("5. Por superficie descendente\n")

    opcion = input("Seleccione una opción: ").strip()
    n = len(lista_paises)

    if n == 0:
        print("No hay países cargados para ordenar.")
    elif opcion in ["1", "2", "3", "4", "5"]:
        if opcion == "1":
            indice = 0   
        elif opcion in ["2", "3"]:
            indice = 1   
        else:
            indice = 2  

        descendente = 0
        if opcion in ["3", "5"]:
            descendente = 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if descendente == 1:
                    if lista_paises[i][indice] < lista_paises[j][indice]:
                        lista_paises[i], lista_paises[j] = lista_paises[j], lista_paises[i]
                else:
                    if lista_paises[i][indice] > lista_paises[j][indice]:
                        lista_paises[i], lista_paises[j] = lista_paises[j], lista_paises[i]

        print("\n Lista ordenada: \n")
        for pais in lista_paises:
            print(f"Nombre: {pais[0]}")
            print(f"Población: {pais[1]}")
            print(f"Superficie: {pais[2]} km²")
            print(f"Continente: {pais[3]}\n")
    else:
        print("Opción invalida.")

def main():
    archivo_paises = os.path.join(os.path.dirname(__file__), "paises.csv")
    paises = cargar_paises(archivo_paises)
    opcion = ""

    while opcion != "10":
        print("\n MENÚ PRINCIPAL \n")
        print("1. Mostrar todos los países")
        print("2. Agregar un país")
        print("3. Actualizar un país")
        print("4. Buscar país por coincidencia parcial")
        print("5. Filtrar por continente")
        print("6. Filtrar por rango de población")
        print("7. Filtrar por rango de superficie")
        print("8. Ordenar por nombre/población/superficie")
        print("9. Mostrar estadísticas")
        print("10. Salir")

        opcion = input("\n Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(archivo_paises)
            paises = cargar_paises(archivo_paises)
        elif opcion == "3":
            actualizar_pais(archivo_paises, paises)
            paises = cargar_paises(archivo_paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_por_continente(paises)
        elif opcion == "6":
            filtrar_por_poblacion(paises)
        elif opcion == "7":
            filtrar_por_superficie(paises)
        elif opcion == "8":
            ordenar_paises(paises)
        elif opcion == "9":
            mostrar_estadisticas(paises)
        elif opcion == "10":
            print("Programa finalizado. ¡Hasta luego!")
        else:
            print("Opción invalida. Intente nuevamente.")

main()