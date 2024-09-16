# Función para fusionar dos sublistas ordenadas
def fusionar(lista_izquierda, lista_derecha):
    lista_ordenada = []
    i = j = 0

    # Comparar elementos de ambas listas y agregar el menor a la lista_ordenada
    while i < len(lista_izquierda) and j < len(lista_derecha):
        if lista_izquierda[i] < lista_derecha[j]:
            lista_ordenada.append(lista_izquierda[i])
            i += 1
        else:
            lista_ordenada.append(lista_derecha[j])
            j += 1

    # Agregar los elementos restantes de ambas listas
    lista_ordenada.extend(lista_izquierda[i:])
    lista_ordenada.extend(lista_derecha[j:])

    return lista_ordenada

# Función de ordenamiento mergesort
def mergesort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    # Fusionar las dos mitades ya ordenadas
    return fusionar(izquierda, derecha)

# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]

print("Lista original:", numeros)

numeros_ordenados = mergesort(numeros)

print("Lista ordenada:", numeros_ordenados)
