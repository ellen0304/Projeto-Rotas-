import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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


class InterfaceGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Planejamento de Rotas de Evacuação")
        self.geometry("800x600")
        
        # Criar o grafo
        self.grafo = nx.Graph()
        self.grafo.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])

        # Configurar a interface
        self.botao_dfs = tk.Button(self, text="Buscar Rota DFS", command=self.buscar_rota_dfs)
        self.botao_dfs.pack()

        self.botao_bfs = tk.Button(self, text="Buscar Rota BFS", command=self.buscar_rota_bfs)
        self.botao_bfs.pack()

        self.figura, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figura, self)
        self.canvas.get_tk_widget().pack()

        # Exibir o grafo na interface
        self.desenhar_grafo()

    def desenhar_grafo(self):
        self.ax.clear()
        pos = nx.spring_layout(self.grafo)
        nx.draw(self.grafo, pos, with_labels=True, ax=self.ax, node_color="lightblue", font_size=10)
        self.canvas.draw()

    def buscar_rota_dfs(self):
        # Usar o algoritmo DFS
        g = Grafo([1, 2, 3, 4, 5])
        g.adicionar_aresta(1, 2)
        g.adicionar_aresta(1, 3)
        g.adicionar_aresta(2, 4)
        g.adicionar_aresta(3, 5)
        
        caminho = g.dfs(1, 5)
        if caminho:
            print(f'Caminho encontrado via DFS: {caminho}')
            self.mostrar_rota(caminho)
        else:
            print("Caminho não encontrado via DFS.")

    def buscar_rota_bfs(self):
        # Usar o algoritmo BFS
        g = Grafo([1, 2, 3, 4, 5])
        g.adicionar_aresta(1, 2)
        g.adicionar_aresta(1, 3)
        g.adicionar_aresta(2, 4)
        g.adicionar_aresta(3, 5)
        
        caminho = g.bfs(1, 5)
        if caminho:
            print(f'Caminho encontrado via BFS: {caminho}')
            self.mostrar_rota(caminho)
        else:
            print("Caminho não encontrado via BFS.")

    def mostrar_rota(self, caminho):
        if caminho:
            print(f"Rota encontrada: {caminho}")
            # Destacar o caminho no grafo
            pos = nx.spring_layout(self.grafo)
            nx.draw(self.grafo, pos, with_labels=True, ax=self.ax, node_color="lightblue", font_size=10)
            caminho_edges = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
            nx.draw_networkx_edges(self.grafo, pos, edgelist=caminho_edges, edge_color="red", width=2)
            self.canvas.draw()


# Rodar a aplicação
if __name__ == "__main__":
    app = InterfaceGrafica()
    app.mainloop()
