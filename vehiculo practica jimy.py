class Vehiculo:
    def __init__(self,marca, modelo):

        self.m = marca
        self.mod = modelo
    
    def obtener_info(self):
        return f"Tengo un {self.m}, modelo {self.mod}"
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.c = color
    
    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre}, Color {self.c}"
    

coche = Coche("chevrolet", "2009", "Gris Bretaña")
print(coche.obtener_info())
     
    
