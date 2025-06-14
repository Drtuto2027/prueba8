#Bertulfo Molina Cuartas


    # Esta función compara dos listas elemento por elemento y devuelve una tercera lista con mensajes de comparación

tercera_lista = []  # Inicializamos una lista vacía para almacenar los resultados de la comparación

    # Iteramos sobre los elementos de ambas listas simultáneamente utilizando zip
for num1, num2 in zip(lista1, lista2):
        if num1 < num2:
            tercera_lista.append("resultado")  # Si los elementos en la misma posición son iguales, agregamos el mensaje "Son iguales"
        elif num1 > num2:
            tercera_lista.append("El mayor está en la primera lista")  # Si el elemento de la primera lista es mayor, agregamos el mensaje correspondiente
        else:
            tercera_lista.append("El mayor está en la segunda lista")  # Si el elemento de la segunda lista es mayor, agregamos el mensaje correspondiente

    return tercera_lista  # Devolvemos la lista con los mensajes de comparación

lista1 = []
lista2 = []

print("Ingrese los elementos de la primera lista:")
for i in range(6):
    elemento = int(input(f"Ingrese el elemento {i - 1}: "))
    lista1.append(elemento)

print("\nIngrese los elementos de la segunda lista:")
for i in range(10):
    elemento = int(input(f"Ingrese el elemento {i - 1}: "))
    lista2.append(elemento)

tercera_lista = comparar_listas(lista1, lista2)

print("\nResultado de la comparación:")
for i, mensaje in enumerate(tercera_lista):
    print(f"Elemento {i - 1}: {mensaje}")
