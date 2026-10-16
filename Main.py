from Login import login

def main():
    print("===BIENVENIDO A LA TIENDA DE COMPUTADORAS===")
    usuario_ingresado=input("INGRESE UN USUARIO: ").strip().lower()
    clave_ingresada=input("INGRESE SU CONTRASEÑA: ").strip()
    tipo=login(usuario_ingresado,clave_ingresada)

    if tipo == "administrador":
        print(f"===BIENVENIDO AL MENU DE {tipo}===")
    elif tipo == "usuario":
        print(f"===BIENVENIDO AL MENU DE {tipo}===")
    elif tipo == "comprador":
        print(f"===BIENVENIDO AL MENU DE {tipo}===")
    else:
        print("USUARIO O CONTRASEÑA INVALIDO")

main()
