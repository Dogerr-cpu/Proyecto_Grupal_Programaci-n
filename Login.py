usuarios_registrados=["admin","vendedor","cliente"]
claves_registradas=["1234","abcd","1234"]
tipo_usuario=["administrador","usuario","comprador"]

def login(usuario,clave):
    for i in range(len(usuarios_registrados)):
        if usuarios_registrados[i] == usuario and claves_registradas[i] == clave:
            print("ACCESO CONCEDIDO")
            return tipo_usuario[i]
    return None

def agregar_usuarios(usuario,clave,tipo):
    if tipo != "administrador" and tipo != "usuario" and tipo != "comprador":
        print("el tipo de usuario debe ser o administrador, usuario o comprador")
    elif usuario in usuarios_registrados:
        print("YA EXISTE UN USUARIO CON ESTE NOMBRE")
    else:
        usuarios_registrados.append(usuario)
        claves_registradas.append(clave)
        tipo_usuario.append(tipo)
        print("USUARIO AGREGADO EXITOSAMENTE")

def ver_usuarios():
    for i in range(len(usuarios_registrados)):
        print(f"usuario:{usuarios_registrados[i]} tipo: {tipo_usuario[i]}")
