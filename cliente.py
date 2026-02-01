from data_manager import cargar_usuarios, guardar_usuario, guardar_ruta_cliente
from utils.validaciones import contraseña_segura
from utils.algoritmos import dijkstra

def registro():
    print("\n--- REGISTRO DE CLIENTE ---")
    nombre = input("Nombre completo: ")
    identificacion = input("ID: ")
    edad = input("Edad: ")
    usuario = input("Correo: ")
    while True:
        password = input("Contraseña: ")
        if contraseña_segura(password):
            break
        print("Contraseña insegura. Debe tener minúscula, mayúscula y número.")
    guardar_usuario({
        "nombre": nombre,
        "identificacion": identificacion,
        "edad": edad,
        "usuario": usuario,
        "password": password
    })
    print("Registro exitoso!")

def login_clientes():
    usuarios = cargar_usuarios()
    print("\n--- LOGIN CLIENTE ---")
    usuario = input("Usuario (correo): ")
    password = input("Contraseña: ")
    for u in usuarios:
        if u["usuario"] == usuario and u["password"] == password:
            print(f"Bienvenido {u['nombre']}!")
            return u
    print("Credenciales incorrectas")
    return None

def menu_cliente(grafo, centros):
    cliente = login_clientes()
    if not cliente:
        return
    seleccion = []

    while True:
        print("\n--- MENU CLIENTE ---")
        print("1. Seleccionar centros para envío")
        print("2. Calcular ruta más económica")
        print("3. Salir")
        op = input("Opción: ")

        if op == "1":
            # Mostrar todos los centros disponibles
            print("\nCentros disponibles:")
            for c in centros:
                print(f"{c['id']} | {c['nombre']} | {c['region']} | {c['subregion']}")
            
            centro = input("Ingrese ID del centro a agregar: ").upper()
            ids = [c['id'].upper() for c in centros]
            if centro not in ids:
                print("ID inválido, el centro no existe.")
                continue

            if centro not in seleccion:
                seleccion.append(centro)
                print("Centro agregado correctamente.")
            else:
                print("El centro ya fue seleccionado.")

            print("Centros seleccionados:", seleccion)

        elif op == "2":
            if len(seleccion) < 2:
                print("Seleccione al menos 2 centros")
                continue
            origen = seleccion[0]
            destino = seleccion[-1]
            if origen not in grafo or destino not in grafo:
                print("Los centros seleccionados no están en el grafo de rutas.")
                continue
            costo, ruta = dijkstra(grafo, origen, destino)
            print("Ruta óptima:", " -> ".join(ruta))
            print("Costo total:", costo)
            guardar_ruta_cliente(cliente["nombre"], ruta, costo)
        elif op == "3":
            break
        else:
            print("Opción inválida")
