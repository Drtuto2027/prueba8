# Clase base Componente
class Componente:
    def ejecutar(self):
        raise NotImplementedError("Debe implementarse en la subclase.")

# Componentes concretos
class ComponenteA(Componente):
    def ejecutar(self):
        print("Ejecutando Componente A.")

class ComponenteB(Componente):
    def ejecutar(self):
        print("Ejecutando Componente B.")

class ComponenteC(Componente):
    def ejecutar(self):
        print("Ejecutando Componente C.")

# Clase Controlador
class Controlador:
    def __init__(self):
        self.componentes = {}
        self.dependencias = {}

    def registrar_componente(self, nombre, componente, dependencias=[]):
        self.componentes[nombre] = componente
        self.dependencias[nombre] = dependencias

    def ejecutar_componente(self, nombre):
        if nombre not in self.componentes:
            print(f"Error: El componente '{nombre}' no está registrado.")
            return
        
        # Verificar dependencias
        dependencias = self.dependencias.get(nombre, [])
        for dep in dependencias:
            if dep not in self.componentes:
                print(f"Error: La dependencia '{dep}' no está registrada.")
                return
            # Ejecutar dependencias primero
            self.ejecutar_componente(dep)
        
        # Ejecutar el componente
        print(f"Ejecutando {nombre}...")
        self.componentes[nombre].ejecutar()

# Ciclo de ejecución
if __name__ == "__main__":
    controlador = Controlador()

    # Registrar componentes
    controlador.registrar_componente("componenteA", ComponenteA(), [])
    controlador.registrar_componente("componenteB", ComponenteB(), ["componenteA"])  # ComponenteB depende de A
    controlador.registrar_componente("componenteC", ComponenteC(), ["componenteB"])  # ComponenteC depende de B

    # Ejecutar componentes
    controlador.ejecutar_componente("componenteC")  # Esto ejecutará A, luego B, luego C
