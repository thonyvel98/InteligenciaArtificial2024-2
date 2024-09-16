# Función de ordenamiento por selección
def ordenamiento_seleccion(lista):
    # Recorre toda la lista
    for i in range(len(lista)):
        # Encuentra el índice del menor elemento en la parte no ordenada
        indice_minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        # Intercambia el menor elemento encontrado con el primer elemento no ordenado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

# Ejemplo de uso
numeros = [64, 25, 12, 22, 11]

print("Lista original:", numeros)

ordenamiento_seleccion(numeros)

print("Lista ordenada:", numeros)
