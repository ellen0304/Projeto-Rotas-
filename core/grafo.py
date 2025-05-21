import networkx as nx
import heapq

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.entrada = None
        self.saida = None
        self.incidente = None
        self.incidente2 = None
        self._criar_mapa_fixo()

    def _criar_mapa_fixo(self):
        # Criando 17 salas fixas numeradas de S1 a S17
        salas = [f"S{i}" for i in range(1, 18)]
        for sala in salas:
            self.adicionar_no(sala)

        # Adicionando conexões (arestas) entre salas com pesos variados
        conexoes = [
            ("S1", "S2", 1), ("S2", "S3", 2), ("S3", "S4", 1), ("S4", "S5", 3),
            ("S5", "S6", 2), ("S6", "S7", 1), ("S7", "S8", 2), ("S8", "S9", 1),
            ("S9", "S10", 3), ("S10", "S11", 2), ("S11", "S12", 1),
            ("S2", "S6", 2), ("S3", "S7", 3), ("S4", "S8", 2), ("S5", "S9", 1),
            ("S7", "S13", 1), ("S13", "S14", 2), ("S14", "S15", 1), ("S15", "S16", 2),
            ("S16", "S17", 1), ("S12", "S17", 3)
        ]

        for origem, destino, peso in conexoes:
            self.adicionar_aresta(origem, destino, peso)

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
                    if vizinho != self.incidente and vizinho != self.incidente2:
                        fila.append((vizinho, caminho + [vizinho]))
        return None

    def _dfs_recursivo(self, atual, destino, visitados=None, caminho=None):
        if visitados is None:
            visitados = set()
        if caminho is None:
            caminho = []

        if atual == self.incidente or atual == self.incidente2:
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

            if atual == self.incidente or atual == self.incidente2:
                continue

            for vizinho in self.grafo.neighbors(atual):
                if vizinho == self.incidente or vizinho == self.incidente2:
                    continue
                peso = self.grafo[atual][vizinho].get("weight", 1)
                nova_distancia = dist[atual] + peso
                if nova_distancia < dist[vizinho]:
                    dist[vizinho] = nova_distancia
                    caminho[vizinho] = atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        return dist, caminho

    def obter_rota(self, origem, destino):
        if origem == self.incidente or destino == self.incidente or \
           origem == self.incidente2 or destino == self.incidente2:
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
