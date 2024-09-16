# Función de ordenamiento por inserción
def ordenamiento_insercion(lista):
    # Recorre desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mueve los elementos mayores que la clave una posición hacia adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta la clave en su posición correcta
        lista[j + 1] = clave

# Ejemplo de uso
numeros = [12, 11, 13, 5, 6]

print("Lista original:", numeros)

ordenamiento_insercion(numeros)

print("Lista ordenada:", numeros)
