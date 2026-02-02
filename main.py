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
        print("3. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            menuAdministrador(centros)
        elif opcion == "2":
            while True:
                print("\n--- MENÚ CLIENTE ---")
                print("1. Iniciar sesión")
                print("2. Registrarse")
                print("3. Volver al menú principal")
                opcion_cliente = input("Opción: ")
                if opcion_cliente == "1":
                    menu_cliente(grafo, centros)
                elif opcion_cliente == "2":
                    registro()
                elif opcion_cliente == "3":
                    break
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

main()
