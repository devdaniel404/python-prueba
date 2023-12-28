##Crea una función que tome una lista de números como entrada y devuelva la suma de todos los números pares en la lista. (0.5 punto)
def suma_numeros_pares():
    numeros = input("Ingresa una lista de números separados por espacios: ")
    lista = [int(numero) for numero in numeros.split()]
    
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma
resultado = suma_numeros_pares()
print("la suma los numeros pares de la lista es: ", resultado)