class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre}, Color: {self.color}"

    def conducir(self):
        return f"Conduciendo mi {self.marca} {self.modelo}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre}, Tipo: {self.tipo}"

    def conducir(self):
        return f"Montando mi {self.marca} {self.modelo}"

# Crear instancias de las clases
coche = Coche("Toyota", "Camry", "Rojo")
moto = Moto("Harley-Davidson", "Sportster", "Deportiva")

# Acceder a métodos y atributos heredados
print(coche.obtener_info())  # Se imprimirá "Toyota Camry, Color: Rojo"
print(coche.conducir())       # Se imprimirá "Conduciendo mi Toyota Camry"

print(moto.obtener_info())   # Se imprimirá "Harley-Davidson Sportster, Tipo: Deportiva"
print(moto.conducir())        # Se imprimirá "Montando mi Harley-Davidson Sportster"
