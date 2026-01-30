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
