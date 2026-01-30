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
