def calcular_area_rectangulos():
    contador_mayores_1000 = 0
    continuar = True
    
    while continuar:
        try:
            base = float(input("Ingrese la base del rectángulo en metros: "))
            altura = float(input("Ingrese la altura del rectángulo en metros: "))
            area = base * altura
            print(f"El área del rectángulo es {area} m²")
            
            if area > 1000:
                contador_mayores_1000 += 1
            else:
                continuar = False
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
    
    print(f"Cantidad de rectángulos con área mayor a 1000 m²: {contador_mayores_1000}")

# Ejecutar la función
calcular_area_rectangulos()
