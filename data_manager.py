def cargar_centros():
    centros = []
    try:
        with open("data/centros.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
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
            linea = f"{c['id']},{c['nombre']},{c['region']},{c['subregion']}\n"
            f.write(linea)
