import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from core.grafo import Grafo
from core.simulacao import SimulacaoManager

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RS - Rota Segura")
        self.geometry("1000x700")
        self.configure(bg="#1e1e2f")

        self.grafo = Grafo()
        self.sim_manager = SimulacaoManager()
        self.figura, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.layout_fixo = None  # Layout fixo do grafo
        self.criar_botoes()
        self.desenhar_mapa()

    def criar_botoes(self):
        frame = tk.Frame(self, bg="#1e1e2f")
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        style = {"bg": "#4e4e8b", "fg": "white", "font": ("Arial", 10, "bold"), "width": 25}

        botoes = [
            ("➕ Adicionar Sala/Corredor", self.adicionar_no),
            ("🔗 Conectar Pontos", self.adicionar_aresta),
            ("🏁 Definir Entrada", self.definir_entrada),
            ("🚪 Definir Saída", self.definir_saida),
            ("🔥 Definir Incidente", self.definir_incidente),
            ("🔍 Rota Principal (BFS)", self.buscar_rota_bfs),
            ("🧭 Rota Alternativa (DFS)", self.buscar_rota_dfs),
            ("🛤️ Rota Mais Curta (Dijkstra)", self.buscar_rota_dijkstra),
            ("💾 Salvar Simulação", self.salvar_simulacao),
            ("📂 Carregar Simulação", self.carregar_simulacao),
            ("🧹 Limpar Rotas", self.limpar_rotas)
        ]
        for texto, comando in botoes:
            tk.Button(frame, text=texto, command=comando, **style).pack(pady=5)

    def desenhar_mapa(self, caminho=None, cor='blue'):
        import networkx as nx

        self.ax.clear()
        if self.layout_fixo is None:
            self.layout_fixo = nx.spring_layout(self.grafo.grafo, seed=42)

        pos = self.layout_fixo
        nx.draw(self.grafo.grafo, pos, with_labels=True, ax=self.ax,
                node_color="lightgray", edge_color="gray",
                node_size=2000, font_size=10)

        if caminho:
            edges = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
            nx.draw_networkx_edges(self.grafo.grafo, pos, edgelist=edges, edge_color=cor, width=3, ax=self.ax)
            nx.draw_networkx_nodes(self.grafo.grafo, pos, nodelist=caminho, node_color=cor, ax=self.ax)

        if self.grafo.incidente:
            nx.draw_networkx_nodes(self.grafo.grafo, pos, nodelist=[self.grafo.incidente], node_color='red', ax=self.ax)

        self.ax.set_facecolor('#2b2b40')
        self.canvas.draw()

    def adicionar_no(self):
        nome = simpledialog.askstring("Adicionar Ponto", "Nome do ponto:")
        if nome:
            self.grafo.adicionar_no(nome)
            self.layout_fixo = None
            self.desenhar_mapa()

    def adicionar_aresta(self):
        origem = simpledialog.askstring("Conectar", "Ponto de origem:")
        destino = simpledialog.askstring("Conectar", "Ponto de destino:")
        if origem and destino:
            self.grafo.adicionar_aresta(origem, destino)
            self.desenhar_mapa()

    def definir_entrada(self):
        ponto = simpledialog.askstring("Entrada", "Qual ponto é a entrada?")
        if ponto:
            self.grafo.entrada = ponto
            messagebox.showinfo("Entrada Definida", f"Entrada definida como: {ponto}")

    def definir_saida(self):
        ponto = simpledialog.askstring("Saída", "Qual ponto é a saída?")
        if ponto:
            self.grafo.saida = ponto
            messagebox.showinfo("Saída Definida", f"Saída definida como: {ponto}")

    def definir_incidente(self):
        ponto = simpledialog.askstring("Incidente", "Onde está o incidente?")
        if ponto:
            self.grafo.incidente = ponto
            messagebox.showinfo("Incidente Definido", f"Incidente em: {ponto}")
            self.desenhar_mapa()

    def buscar_rota_bfs(self):
        caminho = self.grafo.bfs()
        if caminho:
            self.desenhar_mapa(caminho, cor='skyblue')
            messagebox.showinfo("Rota BFS", " → ".join(caminho))
        else:
            messagebox.showwarning("Erro", "Rota não encontrada.")

    def buscar_rota_dfs(self):
        caminho = self.grafo.dfs()
        if caminho:
            self.desenhar_mapa(caminho, cor='deeppink')
            messagebox.showinfo("Rota DFS", " → ".join(caminho))
        else:
            messagebox.showwarning("Erro", "Rota não encontrada.")

    def buscar_rota_dijkstra(self):
        if self.grafo.entrada and self.grafo.saida:
            rota = self.grafo.obter_rota(self.grafo.entrada, self.grafo.saida)
            if rota:
                self.desenhar_mapa(rota, cor='yellow')
                messagebox.showinfo("Rota Dijkstra", " → ".join(rota))
            else:
                messagebox.showwarning("Erro", "Rota não encontrada.")
        else:
            messagebox.showwarning("Erro", "Entrada e Saída devem ser definidas.")

    def salvar_simulacao(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            self.sim_manager.salvar(filename, self.grafo)

    def carregar_simulacao(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            self.sim_manager.carregar(filename, self.grafo)
            self.layout_fixo = None
            self.desenhar_mapa()

    def limpar_rotas(self):
        self.desenhar_mapa()
