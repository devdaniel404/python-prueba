##suma de todos los N naturales menores o iguales a ese N que son múltiplos de 3 o 5
def suma_multiplos_tres_y_cinco(num):
    suma = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma

num = int(input("Introduce un número: "))
resultado = suma_multiplos_tres_y_cinco(num)
print("La suma de los múltiplos de 3 ó 5 menores o iguales a", num, "es:", resultado)