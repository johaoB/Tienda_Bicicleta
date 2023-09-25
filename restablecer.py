import random

# Base de datos de usuarios y contraseñas (simulada)
usuarios = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2',
    # Agrega más usuarios según sea necesario
}

def restablecer_contrasena():
    usuario = input("Ingrese su nombre de usuario: ")

    if usuario in usuarios:
        nueva_contrasena = generar_contrasena_aleatoria()
        usuarios[usuario] = nueva_contrasena
        print(f"La nueva contraseña para {usuario} es: {nueva_contrasena}")
    else:
        print("Usuario no encontrado.")

def generar_contrasena_aleatoria():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    contrasena = ''.join(random.choice(caracteres) for i in range(12))
    return contrasena

if __name__ == "__main__":
    restablecer_contrasena()
