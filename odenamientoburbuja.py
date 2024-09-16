# Función de ordenamiento por burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ejemplo de uso
numeros = [64, 34, 25, 0, 22, 11, 90]

print("Lista original:", numeros)

ordenamiento_burbuja(numeros)

print("Lista ordenada:", numeros)
