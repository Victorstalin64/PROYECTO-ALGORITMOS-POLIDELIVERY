from admin import menuAdministrador
from cliente import registro, menu_cliente
from data_manager import cargar_centros


def main():
    centros = cargar_centros()

    # Grafo de prueba (ID de centros con costos) esto es un ejemplo ñaño, valores quemados costos porque si
    grafo = {
        "C1": {"C2": 10, "C3": 20},
        "C2": {"C1": 10, "C3": 5},
        "C3": {"C1": 20, "C2": 5}
    }

    while True:
        print("\n--- BIENVENIDO A POLIDELIVERY ---")
        print("1. Administrador")
        print("2. Cliente")
        print("3. Registro cliente")
        print("4. Salir")
        op = input("Opción: ")
        if op == "1":
            menuAdministrador(centros)
        elif op == "2":
            menu_cliente(grafo, centros)
        elif op == "3":
            registro()
        elif op == "4":
            break
        else:
            print("Opción inválida")

main()
