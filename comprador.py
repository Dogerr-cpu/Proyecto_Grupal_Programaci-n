
def menu_comprador(nombre):
    while True:
        print(""" 
        1. Ver productos
        2. Salir del sistema
        """)
        opcion=input("INGRESE UNA OPCION 1-2: ")
        match opcion:
            case "1":
                print ("cargando productos...")
            case "2":
                print("SALIENDO DEL SISTEMA....")
                break
            case _:
                print("INGRESE UNA OPCION VALIDA")