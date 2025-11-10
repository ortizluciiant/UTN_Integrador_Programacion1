archivo="paises.csv"

def inicializar_archivo():
    f = open(archivo, "a", encoding="utf-8")
    f.close()
    
    with open (archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        
        if len(lineas) == 0:
            with open(archivo, "w", encoding="utf-8") as fw:
                fw.write("nombre,poblacion,superficie,continente\n")
            print("Archivo paises.csv creado correctamente")
        else:
            print("Archivo paises.csv encontrado")

def cargar_paises():

    paises=[]
    
    with open(archivo, "r", encoding="utf-8") as f:
        encabezado = next(f)
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                print(f"Línea con formato incorrecto: {linea}")
                continue

            nombre, poblacion, superficie, continente = partes

           
            if not poblacion.isdigit() or not superficie.isdigit():
                print(f"Error en los datos de: {nombre}")
                continue

            pais = {
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": int(superficie),
                "continente": continente
            }

            paises.append(pais)

    return paises

def guardar_paises(paises):

    with open (archivo,"w", encoding="utf-8") as f:
        f.write("nombre,poblacion,superficie,continente,\n")
        for p in paises:
            linea= f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
            f.write(linea)

def agregar_pais(paises):
    nombre=input("Ingrese el nombre del pais: ").strip()
    poblacion=input("Ingrese la poblacion: ").strip()
    superficie=input("Ingrese su superficie: ").strip()
    continente=input("Ingrese el continente: ").strip()

    if nombre =="" or poblacion=="" or superficie=="" or continente =="":
        print("El campo no puede estar vacio")
        return
    
    if not poblacion.isdigit() or not superficie.isdigit():
        print("Poblacion y Superficie deben ser valores numericos")
        return
    
    for p in paises:
        if p["nombre"].lower()==nombre.lower():
            print("El pais ya existe")
            return
    
    nuevo={
        "nombre":nombre,
        "poblacion": int(poblacion),
        "superficie":int(superficie),
        "continente":(continente)

    }
    paises.append(nuevo)
    guardar_paises(paises)
    print("\nEl pais fue agregado correctamente")
    
def actualizar_pais(paises):
    nombre=input("Ingrese el nombre del pais que desea actualizar: ").strip()
    encontrado=False

    for p in paises:
        if p["nombre"].lower()==nombre.lower():
            encontrado=True
            poblacion_nueva=input("Nueva poblacion: ").strip()
            superficie_nueva=input("Nueva superficie: ").strip()

            if not poblacion_nueva.isdigit() or not superficie_nueva.isdigit():
                print("Los valores de Poblacion y superficie deben ser numericas")
                return
            p["poblacion"]=int(poblacion_nueva)
            p["superficie"]=int(superficie_nueva)
            guardar_paises(paises)
            print("Se han actualizado los datos correctamente")
            break

        if not encontrado:
            print("Pais no encontrado")

def buscar_pais(paises):
    nombre=input("Ingrese nombre del pais: ").lower()
    encontrado=[]

    for p in paises :
        if nombre in p["nombre"].lower():
            encontrado.append(p)
    
    if len(encontrado)==0:
        print("No se encontraron paises con ese nombre")
    
    else:
        mostrar_lista(encontrado)

def filtrar_paises(paises):
    print("\nFiltrar países por:")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    opcion = input("Seleccione una opción: ").strip()

    filtrados = []

    if opcion == "1":
        continente = input("Ingrese el continente: ").strip().lower()
        for p in paises:
            if p["continente"].lower() == continente:
                filtrados.append(p)

    elif opcion == "2":
        min_pob = int(input("Ingrese población mínima: "))
        max_pob = int(input("Ingrese población máxima: "))
        for p in paises:
            if min_pob <= p["poblacion"] <= max_pob:
                filtrados.append(p)

    elif opcion == "3":
        min_sup = int(input("Ingrese superficie mínima: "))
        max_sup = int(input("Ingrese superficie máxima: "))
        for p in paises:
            if min_sup <= p["superficie"] <= max_sup:
                filtrados.append(p)
    else:
        print("Opción inválida.")
        return

    if len(filtrados) == 0:
        print("No se encontraron países con esos criterios.")
    else:
        print("\nPaíses filtrados:")
        mostrar_lista(filtrados)

def mostrar_lista(paises):
    
    for p in paises:
        print(f"{p['nombre']} - {p['poblacion']} habitantes - {p['superficie']} km2 - {p['continente']}")

def obtener_nombre(p):
    return p["nombre"]

def obtener_poblacion(p):
    return p["poblacion"]

def obtener_superficie(p):
    return p["superficie"]

def ordenar_nombre(paises):
    n=len(paises)
    for i in range(n-1):
        for j in range(i+1,n):
         if paises[i]["nombre"].lower() > paises[j]["nombre"].lower():
                paises[i], paises[j] = paises[j], paises[i]

    mostrar_lista(paises)

def ordenar_poblacion(paises):
    n=len(paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if paises[i]["poblacion"] > paises[j]["poblacion"]:
                paises[i], paises[j] = paises[j], paises[i]
    mostrar_lista(paises)
   
def ordenar_superficie(paises): 
    n = len(paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if paises[i]["superficie"] > paises[j]["superficie"]:
                paises[i], paises[j] = paises[j], paises[i]
    mostrar_lista(paises)
   


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No se han cargado paises")
        return

    mayor = paises[0]
    menor = paises[0]
    poblacion = 0
    superficie = 0
    continentes = {}

    for p in paises:
        
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p

    
        poblacion += p["poblacion"]
        superficie += p["superficie"]

        
        if p["continente"] in continentes:
            continentes[p["continente"]] += 1
        else:
            continentes[p["continente"]] = 1

   
    promedio_p = poblacion / len(paises)
    promedio_s = superficie / len(paises)


    print("Estadísticas:")
    print(f"\nPaís con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Población promedio: {promedio_p}")
    print(f"Superficie promedio: {promedio_s}")
    print("\nCantidad de países por continente:")

    for i in continentes:
        print(f"{i}: {continentes[i]}")
        


def menu():
    inicializar_archivo()
    paises = cargar_paises()

    while True:
        print("\nMENU:")
        print("\n1. Agregar país")
        print("2. Buscar país")
        print("3. Filtrar pais")
        print("4. Ordenar por nombre")
        print("5. Ordenar por población")
        print("6. Ordenar por superficie")
        print("7. Mostrar estadísticas")
        print("8. Salir")

        opcion = input("\nSeleccione una opción: ").strip()
        

        match opcion:
            case "1":
                agregar_pais(paises)
                paises = cargar_paises() 
            case "2":
                buscar_pais(paises)
            case "3":
                filtrar_paises(paises)
            case "4":
                ordenar_nombre(paises)
            case "5":
                ordenar_poblacion(paises)
            case "6":
                ordenar_superficie(paises)
            case "7":
                mostrar_estadisticas(paises)
            case "8":
                print("Muchas gracias, hasta pronto.")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()