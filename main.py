from data_manager import cargar_centros
from admin import menuAdministrador

def main():
    centros = cargar_centros()

    while True:
        print("\n### BIENVENIDO A POLIDELIVERY ###\n")
        print("1. Administrador")
        print("2. Cliente")
        op = input("Opción: ")

        if op == "1":
            menuAdministrador(centros)
        elif op == "2":
            print("Modo cliente (en desarrollo)")
