class Padre:
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

# Crear un objeto de la clase Hijo
hijo = Hijo()

# Acceder a los métodos y atributos heredados de Padre
print(hijo.color_ojos)         # Se imprimirá "marrón"
print(hijo.tipo_pelo)          # Se imprimirá "rulos"
print(hijo.altura)             # Se imprimirá "media"
print(hijo.voz)                # Se imprimirá "grave"
print(hijo.deporte_preferido)  # Se imprimirá "tenis"

# Llamar a los métodos heredados de Padre
print(hijo.reir())              # Se imprimirá "Jajaja"
print(hijo.caminar())           # Se imprimirá "Caminando con pasos largos y rápidos"

# Llamar al método hobby de Hijo (sobrescrito)
print(hijo.hobby())             # Se imprimirá "Juego videojuegos en mi tiempo libre"
