# Función de Búsqueda en Profundidad (DFS) recursiva
def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()  # Crear un conjunto para los nodos visitados
    visitados.add(inicio)  # Marcar el nodo actual como visitado
    print(inicio, end=" ")  # Mostrar el nodo visitado

    # Recorrer los vecinos del nodo actual
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)  # Llamada recursiva para los vecinos no visitados

# Definir el grafo como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejemplo de uso
print("Recorrido DFS desde el nodo 'A':")
dfs(grafo, 'A')
