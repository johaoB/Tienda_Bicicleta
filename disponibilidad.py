# Definimos un diccionario con las estaciones y la cantidad de bicicletas disponibles
disponibilidad_bicicletas = {
    "Estación A": 10,
    "Estación B": 5,
    "Estación C": 8,
    "Estación D": 12
}

# Función para mostrar la disponibilidad
def mostrar_disponibilidad():
    print("Disponibilidad de bicicletas:")
    for estacion, cantidad in disponibilidad_bicicletas.items():
        print(f"{estacion}: {cantidad} bicicletas disponibles")

# Llamamos a la función para mostrar la disponibilidad
mostrar_disponibilidad()
