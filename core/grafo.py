import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.entrada = None
        self.saida = None
        self.incidente = []
        self.layout_fixo = None  # <-- ADICIONE ESTA LINHA


    def adicionar_no(self, nome):
        self.grafo.add_node(nome)

    def adicionar_aresta(self, origem, destino, peso=1):
        self.grafo.add_edge(origem, destino, weight=peso)

    def bfs(self):
        # Busca em largura para caminho entre entrada e saída, ignorando nós com incidente
        from collections import deque

        if not (self.entrada and self.saida):
            return None

        visitados = set()
        fila = deque([[self.entrada]])

        while fila:
            caminho = fila.popleft()
            no_atual = caminho[-1]

            if no_atual == self.saida:
                return caminho

            for vizinho in self.grafo.neighbors(no_atual):
                if vizinho in visitados:
                    continue
                if self.incidente:
                    if isinstance(self.incidente, list):
                        if vizinho in self.incidente:
                            continue
                    elif vizinho == self.incidente:
                        continue
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])
        return None

    def dfs(self):
        # Busca em profundidade para caminho entre entrada e saída, ignorando nós com incidente
        if not (self.entrada and self.saida):
            return None

        visitados = set()
        caminho = []

        def dfs_rec(no):
            if no == self.saida:
                caminho.append(no)
                return True

            visitados.add(no)
            caminho.append(no)

            for vizinho in self.grafo.neighbors(no):
                if vizinho not in visitados:
                    if self.incidente:
                        if isinstance(self.incidente, list):
                            if vizinho in self.incidente:
                                continue
                        elif vizinho == self.incidente:
                            continue
                    if dfs_rec(vizinho):
                        return True
            caminho.pop()
            return False

        if dfs_rec(self.entrada):
            return caminho
        else:
            return None

    def dijkstra(self, origem, destino, incidente=None):
        # Dijkstra, evitando nós com incidente
        if not (origem and destino):
            return None

        grafo_aux = self.grafo.copy()

        # Remove nós com incidente para evitar caminho passando por eles
        if incidente:
            if isinstance(incidente, list):
                grafo_aux.remove_nodes_from(incidente)
            else:
                if grafo_aux.has_node(incidente):
                    grafo_aux.remove_node(incidente)

        try:
            caminho = nx.dijkstra_path(grafo_aux, origem, destino, weight='weight')
            distancia = nx.dijkstra_path_length(grafo_aux, origem, destino, weight='weight')
            return caminho, distancia
        except nx.NetworkXNoPath:
            return None

