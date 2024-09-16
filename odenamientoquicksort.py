# Función de ordenamiento quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]  # Seleccionar el pivote
        izquierda = [x for x in lista if x < pivote]  # Elementos menores que el pivote
        derecha = [x for x in lista if x > pivote]    # Elementos mayores que el pivote
        iguales = [x for x in lista if x == pivote]   # Elementos iguales al pivote
        # Llamada recursiva para las sublistas
        return quicksort(izquierda) + iguales + quicksort(derecha)

# Ejemplo de uso
numeros = [33, 10, 59, 27, 41, 90, 2]

print("Lista original:", numeros)

numeros_ordenados = quicksort(numeros)

print("Lista ordenada:", numeros_ordenados)
