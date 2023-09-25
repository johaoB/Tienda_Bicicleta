class Login:
    username = []
    password = []

    def __init__(self, username, password):
        self.username.append(username)
        self.password.append(password)

    def authenticate(self, input_username, input_password):
        for i in range(len(self.username)):
            if input_username == self.username[i] and input_password == self.password[i]:
                return True
            
        else:
            return False
        
def menu():
    print("""1) Login
2) Iniciar sesión
3) Cerrar sesión
4) Salir""")

def main():
    while True:
        Ingreso = False
        menu()
        print("\n")
        opc = input("Cual es tu opcion: ")

        if opc == "1":
            usuario = input("Ingrese su usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            user_credentials = Login(usuario, contraseña)
            print("\n")

        if opc == "2":
            if Ingreso == False:
                user = input("Ingrese su usuario: ")
                passw = input("Ingrese su contraseña: ") 
                if user_credentials.authenticate(user, passw):
                    print("Inicio de sesión exitoso.")
                    print("\n")
                    Ingreso = True
                else:
                    print("Credenciales incorrectas.")
                    print("\n")
            else:
                print("La sesión ya ha sido iniciada")
                print("\n")

        if opc == "3":
            if Ingreso == True:
                Ingreso = False
                print("La sesión se ha cerrado con existo")
            else:
                print("Primero debes iniciar sesión, para poder cerrarla")

        if opc == "4":
            break


main()