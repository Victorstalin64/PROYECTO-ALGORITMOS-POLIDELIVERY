from utils.ordenamientos import burbuja
from utils.busquedas import busqueda_lineal
from data_manager import guardar_centros

CENTROS_FILE = "data/centros.txt"

def loginAdministrador():
    while True:
        print("\n--- INGRESE SUS CREDENCIALES DE ADMINISTRADOR ---")
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        if usuario == "admin" and password == "admin123":
            print("¡Acceso correcto! Bienvenido administrador.")
            break
        else:
            print("Credenciales incorrectas. Intenta de nuevo.\n")

def agregar_centro(centros):
    print("\n--- AGREGAR CENTRO ---")
    print("Ingrese el ID del centro (ejemplo: C1, C2, ...)")
    id = input("ID: ").upper()
    for c in centros:
        if c["id"].upper() == id:
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
    guardar_centros(centros)  # Guardado automático
    print("Centro agregado correctamente.")

def listar_centros(centros):
    print("\n--- LISTA DE CENTROS ---")
    for c in centros:
        print(f"{c['id']} | {c['nombre']} | {c['region']} | {c['subregion']}")

def actualizar_centro(centros):
    id = input("ID del centro a actualizar: ").upper()
    for c in centros:
        if c["id"].upper() == id:
            c["nombre"] = input("Nuevo nombre: ")
            c["region"] = input("Nueva región: ")
            c["subregion"] = input("Nueva subregión: ")
            guardar_centros(centros)  # Guardado automático
            print("Centro actualizado.")
            return
    print("Centro no encontrado.")

def eliminar_centro(centros):
    id = input("ID del centro a eliminar: ").upper()
    for c in centros:
        if c["id"].upper() == id:
            centros.remove(c)
            guardar_centros(centros)  # Guardado automático
            print("Centro eliminado.")
            return
    print("Centro no encontrado.")

def listar_centros_ordenados(centros):
    print("\n--- LISTAR CENTROS ORDENADOS ---")
    print("Se usará el método de ordenamiento Burbuja")
    burbuja(centros)
    listar_centros(centros)

def menuAdministrador(centros):
    loginAdministrador()  
    while True:
        print("\n### MENU ADMINISTRADOR ###")
        print("1. Agregar centro")
        print("2. Listar centros")
        print("3. Actualizar centro")
        print("4. Eliminar centro")
        print("5. Listar centros ordenados")
        print("6. Salir")
        op = input("Opción: ")
        match op:
            case "1": agregar_centro(centros)
            case "2": listar_centros(centros)
            case "3": actualizar_centro(centros)
            case "4": eliminar_centro(centros)
            case "5": listar_centros_ordenados(centros)
            case "6": break
            case _: print("Opción inválida")

