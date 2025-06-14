class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, other):
        # Sobrecarga del operador +
        return Complejo(self.real + other.real, self.imaginario + other.imaginario)

    def __repr__(self):
        return f"Complejo({self.real}, {self.imaginario}i)"

# Ejemplo de uso:
c1 = Complejo(1, 2)
c2 = Complejo(3, 4)

c3 = c1 + c2
print(c3)  # Salida: Complejo(4, 6i)
