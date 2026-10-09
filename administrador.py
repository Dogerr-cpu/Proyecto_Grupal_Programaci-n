codigos=[1,2,3]
nombres_productos=["laptop","mouse","teclado"]
precios=[12000,250,600]
stocks=[5,20,10]
while True:
        print(""" 
        1. Ver productos
        2. Agregar producto nuevo
        3. Buscar producto
        4. Salir del sistema
        """)
        try:
            opcion=int(input("INGRESE UNA OPCION 1-3: "))
            match opcion:
                case 1:
                    for i in range(len(nombres_productos)):
                        print(f"EL PRODUCTO {nombres_productos[i]}| codigo: {codigos[i]} | precio {precios[i]} | stock {stocks[i]}")
                case 2:
                    try:
                        codigo=int(input("INGRESE EL CODIGO: "))
                        nombre_producto=input("INGRESE EL NOMBRE: ").strip().lower()
                        precio=int(input("INGRESE EL PRECIO: "))
                        stock=int(input("INGRESE EL STOCK: "))
                        if codigo in codigos:
                            print("ya existe este codigo")
                        elif precio <=0 or stock < 0:
                            print("ponga datos bien")
                        else:
                            codigos.append(codigo)
                            nombres_productos.append(nombre_producto)
                            precios.append(precio)
                            stocks.append(stock)
                            print("PRODUCTO INCLUIDO EXITOSAMENTE")
                    except ValueError:
                        print("===INGRESE NUMEROS ENTEROS===")
                case 3:
                    buscar_producto=input("INGRESA EL NOMBRE DEL PRODUCTO CORRECTO: ").strip()
                    validacion=0
                    for i in range(len(nombres_productos)):
                        if nombres_productos[i] == buscar_producto:
                            print("encontrado con exito")
                            validacion=1
                    if validacion == 0:
                        print("no hay ese producto")
                case 4:
                    print("SALIENDO DEL SISTEMA....")
                    break
                case _:
                    print("INGRESE UNA OPCION VALIDA")
        except ValueError:
            print("intentelo denuevo")