class Bicicleta:
    def __init__(self, id, disponible=True):
        self.id = id
        self.disponible = disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def liberar(self):
        if not self.disponible:
            self.disponible = True
            return True
        else:
            return False

class Reserva:
    def __init__(self, cliente, bicicleta):
        self.cliente = cliente
        self.bicicleta = bicicleta
        self.activa = True

    def pagar(self):
        if self.activa:
            self.activa = False
            return True
        else:
            return False

    def cancelar(self):
        if self.activa:
            self.activa = False
            self.bicicleta.liberar()
            return True
        else:
            return False

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def hacer_reserva(self, bicicleta):
        if bicicleta.reservar():
            return Reserva(self, bicicleta)
        else:
            return None

bicicleta1 = Bicicleta(1)
bicicleta2 = Bicicleta(2)

nombre_cliente = input("Por favor, ingresa tu nombre: ")
telefono_cliente = input("Por favor, ingresa tu número de teléfono: ")

cliente1 = Cliente(nombre_cliente, telefono_cliente)

# bicicletas disponibles
print("Bicicletas disponibles:")
print(f"Bicicleta {bicicleta1.id}: {'Disponible' if bicicleta1.disponible else 'No disponible'}")
print(f"Bicicleta {bicicleta2.id}: {'Disponible' if bicicleta2.disponible else 'No disponible'}")

numero_bicicleta = int(input("Por favor, ingresa el número de la bicicleta que deseas reservar: "))

# Verificar si la bicicleta seleccionada está disponible
if numero_bicicleta == bicicleta1.id:
    bicicleta_seleccionada = bicicleta1
elif numero_bicicleta == bicicleta2.id:
    bicicleta_seleccionada = bicicleta2
else:
    print("La bicicleta seleccionada no está disponible o no existe.")
    bicicleta_seleccionada = None

# Si se seleccionó una bicicleta válida, el cliente hace una reserva
if bicicleta_seleccionada:
    reserva = cliente1.hacer_reserva(bicicleta_seleccionada)

    if reserva:
        print("Reserva creada")
        print(f"Cliente: {reserva.cliente.nombre}")
        print(f"Bicicleta: {reserva.bicicleta.id}")

        # El cliente paga la reserva
        if reserva.pagar():
            print("Reserva pagada")
        else:
            print("La reserva ya está pagada o cancelada")

        # El cliente cancela la reserva
        cancelar_reserva = input("¿Deseas cancelar la reserva? (Sí/No): ")

        if cancelar_reserva.lower() == "sí":
            if reserva.cancelar():
                print("Reserva cancelada")
        else:
            print("La reserva ya está cancelada o no existe")
    else:
        print("La reserva sigue activa")