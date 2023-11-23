# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo")

# Definición de la clase derivada Ave
class Ave(Animal):
    def __init__(self, nombre, tipo_plumaje):
        # Llamamos al constructor de la clase base Animal
        super().__init__(nombre)
        self.tipo_plumaje = tipo_plumaje

    def volar(self):
        print(f"{self.nombre} está volando")

# Definición de la clase derivada Pinguino
class Pinguino(Ave):
    def __init__(self, nombre, tipo_plumaje, color_ala):
        # Llamamos al constructor de la clase base Ave
        super().__init__(nombre, tipo_plumaje)
        self.color_ala = color_ala

    def nadar(self):
        print(f"{self.nombre} está nadando")

# Crear instancias de las clases
animal_generico = Animal("Animal Genérico")
animal_generico.comer()

ave_ejemplo = Ave("Aguilucho", "Plumaje Suave")
ave_ejemplo.comer()
ave_ejemplo.volar()

pinguino_ejemplo = Pinguino("Tux", "Plumaje Grueso", "Negro y Blanco")
pinguino_ejemplo.comer()
pinguino_ejemplo.volar()  # Pueden volar, pero no tan alto como otras aves
pinguino_ejemplo.nadar()  # Pueden nadar debido a que son aves adaptadas al agua
