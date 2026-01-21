def loginMenuAdministrador():
    while True:
        print("\n### LOGIN ADMINISTRADOR ###")
        print("Ingrese sus credenciales de administrador")
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contrasena: ")
        if usuario == "admin" and contrasena == "admin123":
            print("Acceso correcto. Bienvenido administrador.")
            break
        else:
            print("\nCredenciales incorrectas. Intente de nuevo.\n")

def menuAdministrador():
    loginMenuAdministrador()
    while True:
        print("\n### MENU ADMINISTRADOR ###")
        print("1. Agregar nuevos centros de distribución, rutas, distancias y costos")
        print("2. Listar centros y rutas")
        print("3. Consultar un centro especifico")
        print("4. Actualizar informacion de centros")
        print("5. Eliminar centros o rutas")
        print("6. Guardar informacion")
        break

def main():
    while True:
        print("\n### BIENVENIDO A POLIDELIVERY ###\n")
        print("Seleccione su rol")
        print("1. Administrador")
        print("2. Cliente")
        opcion = int(input("Seleccione una opcion: "))
        match opcion:
            case 1:
                menuAdministrador()
            case 2:
                print("\n### MENU CLIENTE ###\n")
            case _:
                print("Opcion no valida, intente de nuevo.\n")

main()