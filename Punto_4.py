##Algoritmo de ordenamiento 
lista =[4,2,5,1,3,18,24,36,4,5,17]
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
ordenada = ordenar_lista(lista)
print("La lista ordenada es: ", ordenada)