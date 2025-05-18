import networkx as nx
import heapq

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.entrada = None
        self.saida = None
        self.incidente = None

    def adicionar_no(self, nome):
        self.grafo.add_node(nome)

    def adicionar_aresta(self, origem, destino, peso=1):
        self.grafo.add_edge(origem, destino, weight=peso)

    def get_layout(self):
        return nx.spring_layout(self.grafo, seed=42)

    def bfs(self):
        if not self.entrada or not self.saida:
            return None

        visitados = set()
        fila = [(self.entrada, [self.entrada])]

        while fila:
            atual, caminho = fila.pop(0)
            if atual == self.saida:
                return caminho
            visitados.add(atual)
            for vizinho in self.grafo.neighbors(atual):
                if vizinho not in visitados and vizinho not in [p for p, _ in fila]:
                    if vizinho != self.incidente:
                        fila.append((vizinho, caminho + [vizinho]))
        return None

    def _dfs_recursivo(self, atual, destino, visitados=None, caminho=None):
        if visitados is None:
            visitados = set()
        if caminho is None:
            caminho = []

        if atual == self.incidente:
            return None

        visitados.add(atual)
        caminho.append(atual)

        if atual == destino:
            return list(caminho)

        for vizinho in self.grafo.neighbors(atual):
            if vizinho not in visitados:
                resultado = self._dfs_recursivo(vizinho, destino, visitados, caminho)
                if resultado:
                    return resultado

        caminho.pop()
        return None

    def dfs(self):
        if not self.entrada or not self.saida:
            return None
        return self._dfs_recursivo(self.entrada, self.saida)

    def dijkstra(self, origem):
        dist = {no: float('inf') for no in self.grafo.nodes}
        caminho = {no: None for no in self.grafo.nodes}
        dist[origem] = 0
        fila = [(0, origem)]

        while fila:
            distancia_atual, atual = heapq.heappop(fila)

            if atual == self.incidente:
                continue

            for vizinho in self.grafo.neighbors(atual):
                if vizinho == self.incidente:
                    continue
                peso = self.grafo[atual][vizinho].get("weight", 1)
                nova_distancia = dist[atual] + peso
                if nova_distancia < dist[vizinho]:
                    dist[vizinho] = nova_distancia
                    caminho[vizinho] = atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        return dist, caminho

    def obter_rota(self, origem, destino):
        if origem == self.incidente or destino == self.incidente:
            return None

        dist, caminho = self.dijkstra(origem)
        if dist[destino] == float('inf'):
            return None

        rota = []
        atual = destino
        while atual is not None:
            rota.append(atual)
            atual = caminho[atual]
        rota.reverse()

        return rota if rota[0] == origem else None
# grafo.py

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
