import heapq

# Mapa do campus com pesos (distâncias)
grafo = {
    "Biblioteca": {"Bloco A": 2, "Bloco B": 4},
    "Bloco A": {"Biblioteca": 2, "Bloco B": 3, "Auditório": 2, "Bloco C": 6},
    "Bloco B": {"Biblioteca": 4, "Bloco A": 3, "Bloco C": 2, "Bloco D": 3},
    "Auditório": {"Bloco A": 2, "Refeitório": 5},
    "Bloco C": {"Bloco A": 6, "Bloco B": 2, "Bloco D": 4, "Saída": 2},
    "Bloco D": {"Bloco B": 3, "Bloco C": 4},
    "Refeitório": {"Auditório": 5, "Saída": 2},
    "Saída": {"Bloco C": 2, "Refeitório": 2}
}

def dijkstra(grafo, inicio):
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]
    anteriores = {v: None for v in grafo}

    while fila:
        dist, atual = heapq.heappop(fila)

        for vizinho, peso in grafo[atual].items():
            nova_dist = dist + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                anteriores[vizinho] = atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias, anteriores

def caminho_mais_curto(anteriores, destino):
    caminho = []
    while destino:
        caminho.insert(0, destino)
        destino = anteriores[destino]
    return caminho