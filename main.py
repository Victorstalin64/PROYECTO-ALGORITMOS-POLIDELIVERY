from admin import menuAdministrador
from cliente import registro, menu_cliente, grafos
from data_manager import cargar_centros


def main():
    centros = cargar_centros()
    grafo = grafos()

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
