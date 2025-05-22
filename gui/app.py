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

        self.iconbitmap('gui/icone.ico')

        self.grafo = Grafo()
        self.sim_manager = SimulacaoManager()
        self.figura, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.layout_fixo = None

        # Histórico único que junta BFS, DFS e Dijkstra
        self.historico_rotas = []

        self.criar_botoes()
        self.desenhar_mapa()

    def criar_botoes(self):
        frame = tk.Frame(self, bg="#1e1e2f")
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        style = {"bg": "#4e4e8b", "fg": "white", "font": ("Arial", 10, "bold"), "width": 25}

        botoes = [
            ("➕ Adicionar Sala/Corredor", self.adicionar_no),
            ("🔗 Conectar Pontos com Distância", self.adicionar_aresta),
            ("🏁 Definir Entrada", self.definir_entrada),
            ("🚪 Definir Saída", self.definir_saida),
            ("🔥 Definir Incidente", self.definir_incidente),
            ("🔍 Rota Principal (BFS)", self.buscar_rota_bfs),
            ("🧭 Rota Alternativa (DFS)", self.buscar_rota_dfs),
            ("🛤️ Rota Mais Curta (Dijkstra)", self.buscar_rota_dijkstra),
            ("📜 Mostrar Histórico", self.mostrar_historico),
            ("💾 Salvar Simulação", self.salvar_simulacao),
            ("📂 Carregar Simulação", self.carregar_simulacao),
            ("🧹 Limpar Rotas", self.limpar_rotas),
            ("🗑️ Limpar Grafo", self.limpar_grafo)
        ]
        for texto, comando in botoes:
            tk.Button(frame, text=texto, command=comando, **style).pack(pady=5)

    def desenhar_mapa(self, caminho=None, cor='blue'):
        import networkx as nx

        self.ax.clear()
        if self.layout_fixo is None:
            self.layout_fixo = nx.spring_layout(self.grafo.grafo, seed=42)

        pos = self.layout_fixo

        # Desenha o grafo normalmente
        nx.draw(self.grafo.grafo, pos, with_labels=True, ax=self.ax,
                node_color="lightgray", edge_color="gray",
                node_size=2000, font_size=10)

        # Desenha pesos das arestas com fundo branco semi-transparente
        edge_labels = {}
        for u, v, d in self.grafo.grafo.edges(data=True):
            peso = d.get('weight', 1)  # Usa peso padrão 1 se não existir
            edge_labels[(u, v)] = f"{peso}"

        nx.draw_networkx_edge_labels(self.grafo.grafo, pos, edge_labels=edge_labels,
                                    font_color='black', font_size=9,
                                    bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7))

        # Desenha caminho se houver
        if caminho:
            edges = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
            nx.draw_networkx_edges(self.grafo.grafo, pos, edgelist=edges, edge_color=cor, width=3, ax=self.ax)
            nx.draw_networkx_nodes(self.grafo.grafo, pos, nodelist=caminho, node_color=cor, ax=self.ax)

        # Destaca nós com incidentes (suporta lista)
        incidentes = self.grafo.incidente
        if incidentes:
            if isinstance(incidentes, list):
                nx.draw_networkx_nodes(self.grafo.grafo, pos, nodelist=incidentes, node_color='red', ax=self.ax)
            else:
                nx.draw_networkx_nodes(self.grafo.grafo, pos, nodelist=[incidentes], node_color='red', ax=self.ax)

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
            peso_str = simpledialog.askstring("Distância", f"Informe a distância entre {origem} e {destino} (em metros):")
            if peso_str is None:
                return
            try:
                peso = float(peso_str)
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
                return

            self.grafo.adicionar_aresta(origem, destino, peso)
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
        ponto = simpledialog.askstring("Incidente", "Onde está o incidente? (Para múltiplos, separe por vírgula)")
        if ponto:
            incidentes = [p.strip() for p in ponto.split(",")]
            self.grafo.incidente = incidentes if len(incidentes) > 1 else incidentes[0]
            messagebox.showinfo("Incidente(s) Definido(s)", f"Incidente(s) em: {self.grafo.incidente}")
            self.desenhar_mapa()

    def buscar_rota_bfs(self):
        if not (self.grafo.entrada and self.grafo.saida):
            messagebox.showwarning("Erro", "Entrada e Saída devem ser definidas.")
            return

        caminho = self.grafo.bfs()
        if caminho:
            self.desenhar_mapa(caminho, cor='skyblue')
            self.historico_rotas.append(("BFS", caminho))
            messagebox.showinfo("Rota BFS", " → ".join(caminho))
        else:
            messagebox.showwarning("Erro", "Rota não encontrada.")

    def buscar_rota_dfs(self):
        if not (self.grafo.entrada and self.grafo.saida):
            messagebox.showwarning("Erro", "Entrada e Saída devem ser definidas.")
            return

        caminho = self.grafo.dfs()
        if caminho:
            self.desenhar_mapa(caminho, cor='deeppink')
            self.historico_rotas.append(("DFS", caminho))
            messagebox.showinfo("Rota DFS", " → ".join(caminho))
        else:
            messagebox.showwarning("Erro", "Rota não encontrada.")

    def buscar_rota_dijkstra(self):
        if not (self.grafo.entrada and self.grafo.saida):
            messagebox.showwarning("Erro", "Entrada e Saída devem ser definidas.")
            return

        resultado = self.grafo.dijkstra(self.grafo.entrada, self.grafo.saida, self.grafo.incidente)
        if resultado is not None:
            rota, distancia = resultado
            self.desenhar_mapa(rota, cor='yellow')
            self.historico_rotas.append(("Dijkstra", rota, distancia))
            messagebox.showinfo("Rota Dijkstra", f"{' → '.join(rota)}\nDistância total: {distancia:.2f} metros")
        else:
            messagebox.showwarning("Erro", "Rota não encontrada.")

    def mostrar_historico(self):
        if not self.historico_rotas:
            messagebox.showinfo("Histórico", "Nenhuma rota calculada ainda.")
            return

        texto = ""
        for item in self.historico_rotas:
            tipo = item[0]
            rota = item[1]
            if tipo == "Dijkstra":
                distancia = item[2]
                texto += f"{tipo}: {' → '.join(rota)} (Distância: {distancia:.2f}m)\n"
            else:
                texto += f"{tipo}: {' → '.join(rota)}\n"

        messagebox.showinfo("Histórico de Rotas", texto)

    def salvar_simulacao(self):
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".json",
                                                      filetypes=[("JSON files", "*.json")])
        if caminho_arquivo:
            try:
                self.sim_manager.salvar(self.grafo, caminho_arquivo)
                messagebox.showinfo("Salvar Simulação", "Simulação salva com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao salvar simulação: {e}")

    def carregar_simulacao(self):
        caminho_arquivo = filedialog.askopenfilename(defaultextension=".json",
                                                    filetypes=[("JSON files", "*.json")])
        if caminho_arquivo:
            try:
                self.grafo = self.sim_manager.carregar(caminho_arquivo)
                # Atualiza o layout fixo para o carregado no grafo
                self.layout_fixo = getattr(self.grafo, 'layout_fixo', None)
                self.historico_rotas.clear()
                self.desenhar_mapa()
                messagebox.showinfo("Carregar Simulação", "Simulação carregada com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao carregar simulação: {e}")

    def limpar_rotas(self):
        self.historico_rotas.clear()
        self.desenhar_mapa()
        messagebox.showinfo("Histórico", "Histórico de rotas limpo.")

    def limpar_grafo(self):
        self.grafo = Grafo()
        self.layout_fixo = None
        self.historico_rotas.clear()
        self.desenhar_mapa()
        messagebox.showinfo("Limpar", "Grafo limpo.")



