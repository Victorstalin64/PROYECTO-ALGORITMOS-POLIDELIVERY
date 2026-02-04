# Importación del método de ordenamiento burbuja
from utils.ordenamientos import burbuja
# Importación del método de búsqueda lineal
from utils.busquedas import busqueda_lineal
# Importación de la función para guardar centros en archivo
from data_manager import guardar_centros
#Muchachos organice un poco todo en general y los deje arriba, modifique un poco el menu y agregue una opción más

# Archivo donde se almacenan los centros de distribución
CENTROS_FILE = "data/centros.txt"
# Permite registrar un nuevo centro de distribución
# Verifica que el ID no esté repetido antes de agregarlo
def agregar_centro(centros):
    print("\n--- AGREGAR CENTRO ---")
    id = input("ID: ")
    for c in centros:
        if c["id"] == id:
            print("ID ya existe.")
            return

    nombre = input("Nombre: ")
    region = input("Región: ")
    subregion = input("Subregión: ")

    centros.append({
        "id": id,
        "nombre": nombre,
        "region": region,
        "subregion": subregion
    })
    guardar_centros(centros)
    print("Centro agregado correctamente.")
    
def listar_centros(centros):
    print("\n--- LISTA DE CENTROS ---")
    for c in centros:
        print(f"{c['id']} | {c['nombre']} | {c['region']} | {c['subregion']}")
        
def actualizar_centro(centros):
    id = input("ID del centro a actualizar: ")
    for c in centros:
        if c["id"] == id:
            c["nombre"] = input("Nuevo nombre: ")
            c["region"] = input("Nueva región: ")
            c["subregion"] = input("Nueva subregión: ")
            guardar_centros(centros)
            print("Centro actualizado.")
            return
    print("Centro no encontrado.")
    
def eliminar_centro(centros):
    id = input("ID del centro a eliminar: ")
    for c in centros:
        if c["id"] == id:
            centros.remove(c)
            guardar_centros(centros)
            print("Centro eliminado.")
            return
    print("Centro no encontrado.")

def listar_centros_ordenados(centros):
    print("\n--- LISTAR CENTROS ORDENADOS ---")
    print("Se usará e método de ordenamiento Burbuja")
    burbuja(centros)
    listar_centros(centros)

def menuAdministrador(centros):
    while True:
        print("\n### MENU ADMINISTRADOR ###")
        print("1. Agregar centro")
        print("2. Listar centros")
        print("3. Actualizar centro")
        print("4. Eliminar centro")
        print("5. Guardar cambios")
        print("6. Listar centros ordenados")
        print("7. Salir")

        op = input("Opción: ")

        match op:
            case "1":
                agregar_centro(centros)
            case "2":
                listar_centros(centros)
            case "3":
                actualizar_centro(centros)
            case "4":
                eliminar_centro(centros)
            case "5":
                guardar_centros(centros)
            case "6":
                listar_centros_ordenados(centros)
            case "7":
                break
            case _:
                print("Opción inválida")



