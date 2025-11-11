Descripcion del Programa
Este programa en Python permite gestionar un archivo csv de paises que contiene informacion sobre nombres, poblacion, superficie y continente
A traves de un Menu interactivo, el usuario puede

*Agregar nuevos paises al archivo
*Buscar paises por nombre
*Ordenar los paises por nombre, poblacion o superficie.
*Calcular estadisticas como promedio, mayor/menor poblacion, cantidad por continente.
*Guardar automaticamente los cambios en el archivo csv.

El sistema usa estructura de datos de tipo Diccionario y maneja el archivo de manera segura, validando errores comunes comocampos vacios, datos no numericos, duplicados, etc.

Instrucciones de uso

1. Debe asegurarse de tener Python instalado.
2. Colocar el archivo paises.csv en el mismo directorio del programa, si el mismo no existe, se crea automaticamente al ejecutar
3. Ejecutar el script

El archivo csv, se genera automaticamente con el siguiente encabezado: nombre,poblacion,superficie,continente.
Ejemplo de contenido :
Argentina,56700000,2780000,America
España,48000000,505000,Europa


Navegacion por el menu usando los numeros de las opciones
1. Agregar pais
2. Buscar pais
3. Ordenar por nombre
4. Ordenar por poblacion
5. Ordenar por superficie (descendente)
6. Mostrar estadisticas
7. Salir

Ejemplos de entrada y salida

*Ejemplo 1)

Entrada - Agregar pais

Ingrese el nombre del pais: Argentina
Ingrese la poblacion: 56700000
Ingrese su superficie: 2780000
Ingrese el continente: America

Salida-

El pais fue agregado correctamente

*Ejemplo 2) - Buscar pais

Ingrese el nombre del pais: argentina

Salida-

Argentina - 56700000 habitantes - 2780000 km2 - America

*Ejemplo 3) - Mostrar estadisticas
(Los siguientes datos son  incluidos a modo de ejemplo para comprender la salida de la opcion del menu - Mostrar estadistica -)

salida-

Estadisticas:
Pais con mayor poblacion: China (1400000000)
Pais con menor poblacion: Uruguay (3500000)
Poblacion promedio: 287000000.0
Superficie promedio: 520000.0

Cantidad de paises por continente:
America: 2
Asia: 3
Europa: 1

DESARROLLO:
Ortiz Lucia:
Implementación de funciones para cargar, agregar y actualizar países en el archivo CSV.
Creación de funciones de búsqueda, ordenamiento 
Desarrollo de la función de estadísticas, incluyendo cálculo de promedios, identificación de países con mayor y menor población, y conteo de países por continente.
Implementación del menú de navegación en consola y control de flujo con match.
Validaciones de entradas de usuario y manejo de errores.

Demarco Ramiro:
Pruebas de funcionamiento del código, verificando que todas las opciones del menú funcionen correctamente.
Evaluación y mejoras del menú
Desarrollo de la función filtrar_paises
Generación de capturas de pantalla y preparación de ejemplos de ejecución.
Mejoras en las funciones de búsqueda y ordenamiento




   
