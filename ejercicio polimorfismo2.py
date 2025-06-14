def suma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Suma de números
        return a + b
    elif isinstance(a, list) and isinstance(b, list):
        # Concatenación de listas
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        # Concatenación de cadenas de texto
        return a + b
    else:
        raise TypeError("Los tipos de datos no son compatibles para la suma.")

# Ejemplos de uso
print(suma(3, 5))           # Suma de números -> 8
print(suma([1, 2], [3, 4])) # Suma de listas -> [1, 2, 3, 4]
print(suma("oe", " yave")) # Suma de cadenas -> "oe yave"
