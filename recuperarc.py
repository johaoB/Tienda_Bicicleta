import getpass

def cambiar_contraseña():
    usuario = input("Introduce tu nombre de usuario: ")
    contraseña_actual = getpass.getpass("Introduce tu contraseña actual: ")
    
    # Aquí puedes agregar código para verificar la contraseña actual
    # Si la contraseña actual no es correcta, puedes mostrar un mensaje de error y salir
    
    nueva_contraseña = getpass.getpass("Introduce tu nueva contraseña: ")
    confirmar_contraseña = getpass.getpass("Confirma tu nueva contraseña: ")
    
    if nueva_contraseña == confirmar_contraseña:
        # Aquí puedes agregar código para actualizar la contraseña en tu sistema
        print("Contraseña actualizada correctamente")
    else:
        print("Las contraseñas no coinciden. Inténtalo de nuevo.")

# Llama a la función para cambiar la contraseña
cambiar_contraseña()
