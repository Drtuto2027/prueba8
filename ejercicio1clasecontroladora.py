class Suma:
    def calcular(self, num1, num2):
        return num1 + num2

class Resta:
    def calcular(self, num1, num2):
        return num1 - num2

class Multiplicacion:
    def calcular(self, num1, num2):
        return num1 * num2

class Division:
    def calcular(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        return num1 / num2

class CalculadoraControlador:
    def __init__(self):
        self.operaciones = {
            'suma': Suma(),
            'resta': Resta(),
            'multiplicacion': Multiplicacion(),
            'division': Division()
        }

    def iniciar_calculadora(self):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            
            print("\nOperaciones disponibles:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            operacion = input("Selecciona la operación (1/2/3/4): ")
            
            if operacion == '1':
                resultado = self.sumar(num1, num2)
            elif operacion == '2':
                resultado = self.restar(num1, num2)
            elif operacion == '3':
                resultado = self.multiplicar(num1, num2)
            elif operacion == '4':
                resultado = self.dividir(num1, num2)
            else:
                print("Opción no válida.")
                return

            print(f"El resultado es: {resultado}")
        
        except ValueError:
            print("Error: Por favor ingresa números válidos.")

    def sumar(self, num1, num2):
        return self.operaciones['suma'].calcular(num1, num2)

    def restar(self, num1, num2):
        return self.operaciones['resta'].calcular(num1, num2)

    def multiplicar(self, num1, num2):
        return self.operaciones['multiplicacion'].calcular(num1, num2)

    def dividir(self, num1, num2):
        return self.operaciones['division'].calcular(num1, num2)

if __name__ == "__main__":
    calculadora = CalculadoraControlador()
    calculadora.iniciar_calculadora()
