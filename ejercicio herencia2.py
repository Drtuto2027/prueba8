# Definir clases para objetos
class Campana:
    def sonido(self):
        return "La campana suena: ding dong."

class Radio:
    def sonido(self):
        return "La radio suena: música y noticias."

class Telefono:
    def sonido(self):
        return "El teléfono suena: ring ring."

class Coche:
    def sonido(self):
        return "El coche suena: beep beep."

# Crear una lista con instancias de objetos
objetos = [Campana(), Radio(), Telefono(), Coche()]

# Recorrer la lista e imprimir el sonido de cada objeto
for objeto in objetos:
    print(objeto.sonido())
