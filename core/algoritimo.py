# algoritmos.py

import heapq

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
