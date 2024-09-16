# Función de búsqueda binaria
def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Encontrar el punto medio
        if lista[medio] == valor:
            return medio  # Devuelve el índice si se encuentra el valor
        elif lista[medio] < valor:
            inicio = medio + 1  # Buscar en la mitad derecha
        else:
            fin = medio - 1  # Buscar en la mitad izquierda

    return -1  # Devuelve -1 si no se encuentra el valor

# Ejemplo de uso
numeros_ordenados = [12, 22, 10, 23, 45, 70, 80, 99, 120, 11, 22, 33]
valor_a_buscar = 70

resultado = busqueda_binaria(numeros_ordenados, valor_a_buscar)

if resultado != -1:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no está en la lista.")
