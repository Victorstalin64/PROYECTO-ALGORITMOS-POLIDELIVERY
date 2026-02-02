import os


def cargar_centros():
    centros = []
    try:
        with open("data/centros.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) >= 4:
                    centros.append({
                        "id": datos[0],
                        "nombre": datos[1],
                        "region": datos[2],
                        "subregion": datos[3]
                    })
    except FileNotFoundError:
        pass
    return centros

def guardar_centros(centros):
    with open("data/centros.txt", "w", encoding="utf-8") as f:
        for c in centros:
            f.write(f"{c['id']},{c['nombre']},{c['region']},{c['subregion']}\n")


def cargar_usuarios():
    usuarios = []
    try:
        with open("data/usuarios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) >= 5:
                    usuarios.append({
                        "nombre": datos[0],
                        "identificacion": datos[1],
                        "edad": datos[2],
                        "usuario": datos[3],
                        "password": datos[4]
                    })
    except FileNotFoundError:
        pass
    return usuarios

def guardar_usuario(usuario):
    with open("data/usuarios.txt", "a", encoding="utf-8") as f:
        f.write(f"{usuario['nombre']},{usuario['identificacion']},{usuario['edad']},{usuario['usuario']},{usuario['password']}\n")


def guardar_ruta_cliente(nombre_cliente, ruta, costo):
    nombre_archivo = f"data/rutas-{nombre_cliente}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Ruta seleccionada:{' -> '.join(ruta)}\n")
        f.write(f"Costo total: {costo}\n")
