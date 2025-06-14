class Coche:
    def __init__(self, marca, modelo, año):
        # Atributos de instancia (estado interno del objeto)
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False  # Estado inicial del coche

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El coche {self.marca} {self.modelo} está encendido.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El coche {self.marca} {self.modelo} está apagado.")
        else:
            print(f"El coche {self.marca} {self.modelo} ya está apagado.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"El coche {self.marca} {self.modelo} está {estado}.")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2022)

# Ver el estado interno del coche
mi_coche.mostrar_estado()  # Apagado por defecto

# Encender el coche y ver el estado
mi_coche.encender()
mi_coche.mostrar_estado()

# Apagar el coche y ver el estado
mi_coche.apagar()
mi_coche.mostrar_estado()
