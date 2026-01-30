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
            print("Centro actualizado.")
            return
    print("Centro no encontrado.")
def eliminar_centro(centros):
    id = input("ID del centro a eliminar: ")
    for c in centros:
        if c["id"] == id:
            centros.remove(c)
            print("Centro eliminado.")
            return
    print("Centro no encontrado.")
from data_manager import guardar_centros

def menuAdministrador(centros):
    while True:
        print("\n### MENU ADMINISTRADOR ###")
        print("1. Agregar centro")
        print("2. Listar centros")
        print("3. Actualizar centro")
        print("4. Eliminar centro")
        print("5. Guardar cambios")
        print("6. Salir")

        op = input("Opción: ")

        if op == "1":
            agregar_centro(centros)
        elif op == "2":
            listar_centros(centros)
        elif op == "3":
            actualizar_centro(centros)
        elif op == "4":
            eliminar_centro(centros)
        elif op == "5":
            guardar_centros(centros)
        elif op == "6":
            break
from utils.ordenamientos import burbuja

def listar_centros_ordenados(centros):
    burbuja(centros)
    listar_centros(centros)
