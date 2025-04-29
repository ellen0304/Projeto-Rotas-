import networkx as nx
from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = {v: [] for v in vertices}

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)  # Grafo não direcionado

    # Algoritmo DFS
    def dfs(self, inicio, objetivo, visitado=None, caminho=None):
        if visitado is None:
            visitado = set()
        if caminho is None:
            caminho = []
        
        visitado.add(inicio)
        caminho.append(inicio)

        if inicio == objetivo:
            return caminho
        
        for vizinho in self.grafo[inicio]:
            if vizinho not in visitado:
                novo_caminho = self.dfs(vizinho, objetivo, visitado, caminho.copy())
                if novo_caminho:
                    return novo_caminho
        return None

    # Algoritmo BFS
    def bfs(self, inicio, objetivo):
        fila = deque([inicio])
        visitado = set([inicio])
        caminho = {inicio: None}

        while fila:
            atual = fila.popleft()
            if atual == objetivo:
                # Reconstruir o caminho
                caminho_encontrado = []
                while atual is not None:
                    caminho_encontrado.append(atual)
                    atual = caminho[atual]
                return caminho_encontrado[::-1]
            
            for vizinho in self.grafo[atual]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    fila.append(vizinho)
                    caminho[vizinho] = atual
        return None
