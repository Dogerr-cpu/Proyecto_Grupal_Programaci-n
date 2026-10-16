usuarios_registrados=["admin","vendedor","cliente"]
claves_registradas=["1234","abcd","1234"]
tipo_usuario=["administrador","usuario","comprador"]

def login(usuario,clave):
    for i in range(len(usuarios_registrados)):
        if usuarios_registrados[i] == usuario and claves_registradas[i] == clave:
            print("ACCESO CONCEDIDO")
            return tipo_usuario[i]
    return None