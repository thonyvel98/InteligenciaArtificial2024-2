# Función de búsqueda lineal
def busqueda_lineal(lista, valor):
    for indice in range(len(lista)):
        if lista[indice] == valor:
            return indice  # Devuelve el índice donde se encuentra el valor
    return -1  # Devuelve -1 si el valor no está en la lista

# Ejemplo de uso
numeros = [10, 23, 45, 70, 11, 15]
valor_a_buscar = 70

resultado = busqueda_lineal(numeros, valor_a_buscar)

if resultado != -1:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no está en la lista.")
