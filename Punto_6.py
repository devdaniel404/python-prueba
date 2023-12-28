#listado de numeros comunes
def elementos_comunes(lista1, lista2):
    elementos = []
    for elemento in lista1:
        if elemento in lista2:
            elementos.append(elemento)
    return elementos

# Solicitar la primera lista al usuario
entrada1 = input("Ingresa los elementos de la primera lista separados por espacios: ")
lista1 = entrada1.split()  # Convierte la entrada en una lista de strings
lista1 = [int(elemento) for elemento in lista1]  # Convierte los elementos a enteros

# Solicitar la segunda lista al usuario
entrada2 = input("Ingresa los elementos de la segunda lista separados por espacios: ")
lista2 = entrada2.split()  # Convierte la entrada en una lista de strings
lista2 = [int(elemento) for elemento in lista2]  # Convierte los elementos a enteros

# Encontrar los elementos comunes
elementos_comunes = elementos_comunes(lista1, lista2)
print("Elementos comunes:", elementos_comunes)