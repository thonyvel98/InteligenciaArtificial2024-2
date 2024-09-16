from collections import deque

# Función de Búsqueda en Anchura (BFS)
def bfs(grafo, inicio):
    # Crear una cola para el BFS
    cola = deque([inicio])
    # Conjunto de nodos visitados
    visitados = set([inicio])

    while cola:
        # Sacar un nodo de la cola
        nodo = cola.popleft()
        print(nodo, end=" ")  # Mostrar el nodo visitado

        # Recorrer los vecinos del nodo actual
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                # Si no se ha visitado, añadirlo a la cola y marcarlo como visitado
                visitados.add(vecino)
                cola.append(vecino)

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
print("Recorrido BFS desde el nodo 'A':")
bfs(grafo, 'A')
