import networkx as nx
import random

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.entrada = None
        self.saida = None
        self.incidente = None
        self.nx = nx

    def adicionar_no(self, nome):
        self.grafo.add_node(nome)

    def adicionar_aresta(self, origem, destino):
        self.grafo.add_edge(origem, destino)

    def get_layout(self):
        return nx.spring_layout(self.grafo, seed=42)

    def dfs(self):
        if not self.entrada or not self.saida:
            return None
        return self._dfs_recursivo(self.entrada, self.saida)

    def _dfs_recursivo(self, atual, destino, visitado=None, caminho=None):
        if visitado is None:
            visitado = set()
        if caminho is None:
            caminho = []
        visitado.add(atual)
        caminho.append(atual)
        if atual == destino:
            return caminho
        for vizinho in random.sample(list(self.grafo[atual]), len(self.grafo[atual])):
            if vizinho not in visitado:
                novo_caminho = self._dfs_recursivo(vizinho, destino, visitado, caminho.copy())
                if novo_caminho:
                    return novo_caminho
        return None

    def bfs(self):
        if not self.entrada or not self.saida:
            return None
        fila = [self.entrada]
        visitado = {self.entrada}
        anterior = {self.entrada: None}
        while fila:
            atual = fila.pop(0)
            if atual == self.saida:
                caminho = []
                while atual:
                    caminho.append(atual)
                    atual = anterior[atual]
                return caminho[::-1]
            for vizinho in self.grafo[atual]:
                if vizinho not in visitado:
                    fila.append(vizinho)
                    visitado.add(vizinho)
                    anterior[vizinho] = atual
        return None
