# Definición de la clase base A
class A:
    def __init__(self, valor_a):
        self.valor_a = valor_a

    def mostrar_valor_a(self):
        print(f"Valor de A: {self.valor_a}")

# Definición de la clase base B
class B:
    def __init__(self, valor_b):
        self.valor_b = valor_b

    def mostrar_valor_b(self):
        print(f"Valor de B: {self.valor_b}")

# Definición de la clase derivada C que hereda de A y B
class C(A, B):
    def __init__(self, valor_a, valor_b, valor_c):
        # Llamamos a los constructores de las clases base A y B
        A.__init__(self, valor_a)
        B.__init__(self, valor_b)
        self.valor_c = valor_c

    def mostrar_valor_c(self):
        print(f"Valor de C: {self.valor_c}")

# Crear una instancia de la clase derivada C
objeto_c = C(valor_a=1, valor_b=2, valor_c=3)

# Acceder a los métodos de las clases base A y B a través de la clase derivada C
objeto_c.mostrar_valor_a()  # Mostrará "Valor de A: 1"
objeto_c.mostrar_valor_b()  # Mostrará "Valor de B: 2"

# Acceder a los métodos de la clase derivada C
objeto_c.mostrar_valor_c()  # Mostrará "Valor de C: 3"
