##invertir texto
def invertir_cadena(cadena):
    return cadena[::-1]

cadena = input("Ingrese oración a invertir: ") #oración de ingreso por el usuario
cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida) # salida invertida