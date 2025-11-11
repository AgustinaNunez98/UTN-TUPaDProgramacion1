Descripción del programa

Este proyecto forma parte del Trabajo Práctico Integrador de la materia Programación 1 de la Tecnicatura Universitaria en Programación (UTN).
El programa permite gestionar información sobre países mediante operaciones de carga, búsqueda, actualización, filtrado, ordenamiento y generación de estadísticas.

Los datos se almacenan en un archivo CSV y se manipulan en memoria utilizando listas y funciones. El menú principal en consola ofrece una interfaz simple y modular que facilita la interacción con el usuario.

Objetivos principales
	•	Aplicar estructuras de datos en Python (listas y diccionarios).
	•	Implementar funciones con responsabilidades únicas.
	•	Utilizar condicionales, ciclos, ordenamientos y manejo de archivos CSV.
	•	Generar estadísticas básicas a partir de un conjunto de datos.

⸻

Instrucciones de uso
1. Al iniciar, se cargará el archivo paises.csv con los datos existentes.
El menú principal mostrará las siguientes opciones:

1. Mostrar todos los países
2. Agregar un país
3. Actualizar un país
4. Buscar país por coincidencia parcial
5. Filtrar por continente
6. Filtrar por rango de población
7. Filtrar por rango de superficie
8. Ordenar por nombre/población/superficie
9. Mostrar estadísticas
10. 

2. Seleccionar una opción ingresando el número correspondiente.
El sistema validará los datos y mostrará mensajes claros de error o éxito.

Ejemplos de entradas y salidas

Ejemplo 1 – Agregar un país
Ingrese el nombre del país: Chile
Ingrese la población: 19212362
Ingrese la superficie: 756096
Ingrese el continente: América
País 'Chile' agregado correctamente al archivo.

Ejemplo 2 – Buscar país
Ingrese el nombre del país a buscar: jap
País encontrado
Nombre: Japón
Población: 125800000
Superficie: 377975 km²
Continente: Asia

Ejemplo 3 – Filtrar por población
Ingrese la población mínima: 10000000
Ingrese la población máxima: 50000000
Países con población entre 10000000 y 50000000:
Argentina – 45376763
Chile – 19212362

Ejemplo 4 – Estadísticas
País con mayor población: Japón - 125800000
País con menor población: Chile - 19212362
Población promedio: 63396375
Cantidad de países por continente:
América: 2
Asia: 1
Europa: 1

Participación
Integrante: Agustina Antigona Nuñez
Rol: Desarrolladora principal
Tareas principales: Codificación del sistema, validaciones, estructura del menú, manejo de archivos CSV, redacción del marco teórico y documentación.