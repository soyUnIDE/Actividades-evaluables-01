import hashlib

# Función para convertir la contraseña a formato hash (SHA-256)
def convertir_a_hash(contrasena):
    sha256 = hashlib.sha256()
    sha256.update(contrasena.encode('utf-8'))
    return sha256.hexdigest()

# Utilizando una lista para almacenar usuarios y contraseñas
usuarios_lista = []
contrasenas_lista = []

# Llenar la lista con 5 usuarios y contraseñas
usuarios_lista.extend(["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"])
contrasenas_original = ["pass123", "qwerty", "password", "securepass", "123456"]

# Convertir las contraseñas a formato hash y almacenarlas en la lista
for contrasena in contrasenas_original:
    contrasena_hash = convertir_a_hash(contrasena)
    contrasenas_lista.append(contrasena_hash)

# Consulta 1: Verificar si un usuario y su contraseña coinciden (utilizando la lista)
usuario_consulta1 = "usuario3"
contrasena_consulta1 = "password"
contrasena_hash_consulta1 = convertir_a_hash(contrasena_consulta1)

if usuario_consulta1 in usuarios_lista and contrasena_hash_consulta1 in contrasenas_lista:
    print(f"Acceso permitido para {usuario_consulta1}.")
else:
    print(f"Acceso denegado para {usuario_consulta1}.")

# Utilizando un diccionario para almacenar usuarios y contraseñas
usuarios_diccionario = {}
contrasenas_diccionario = {}

# Llenar el diccionario con 5 usuarios y contraseñas
for i in range(5):
    usuario = f"usuario{i + 1}"
    contrasena_original = f"pass{i + 1}"
    contrasena_hash = convertir_a_hash(contrasena_original)

    usuarios_diccionario[usuario] = contrasena_hash
    contrasenas_diccionario[usuario] = contrasena_hash

# Consulta 2: Verificar si un usuario y su contraseña coinciden (utilizando el diccionario)
usuario_consulta2 = "usuario2"
contrasena_consulta2 = "qwerty"
contrasena_hash_consulta2 = convertir_a_hash(contrasena_consulta2)

if usuario_consulta2 in usuarios_diccionario and contrasena_hash_consulta2 == contrasenas_diccionario[usuario_consulta2]:
    print(f"Acceso permitido para {usuario_consulta2}.")
else:
    print(f"Acceso denegado para {usuario_consulta2}.")