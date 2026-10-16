codigos=[1,2,3]
nombres_productos=["laptop","mouse","teclado"]
precios=[12000,250,600]
stocks=[5,20,10]

def ver_productos():
    print("===PRODUCTOS DISPONIBLES===")
    for i in range(len(codigos)):
        print(f"CODIGO {codigos[i]}: {nombres_productos[i]} - PRECIO: ${precios[i]} - STOCK: {stocks[i]}")

def buscar_producto(codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1

def agregar_producto(codigo,nombre,precio,stock):
    if buscar_producto(codigo) != -1:
        print("ESE CODIGO YA EXISTE")
    elif precio <= 0 or stock < 0:
        print("INGRESE DATOS VALIDOS")
    else:
        codigos.append(codigo)
        nombres_productos.append(nombre)
        precios.append(precio)
        stocks.append(stock)
        print("PRODUCTO AGREGADO")