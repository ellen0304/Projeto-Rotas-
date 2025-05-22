import json
from core.grafo import Grafo

class SimulacaoManager:
    def salvar(self, grafo, caminho_arquivo):
        # Monta estrutura de nós e arestas no formato que você mostrou
        nos = list(grafo.grafo.nodes)
        arestas = []
        for u, v, dados in grafo.grafo.edges(data=True):
            peso = dados.get('weight', 1.0)
            arestas.append({
                "origem": u,
                "destino": v,
                "peso": peso
            })

        # Salva posições do layout fixo (se existir)
        pos = None
        if hasattr(grafo, 'layout_fixo') and grafo.layout_fixo:
            pos = {str(k): [float(v[0]), float(v[1])] for k, v in grafo.layout_fixo.items()}

        salvar_dados = {
            "nos": nos,
            "arestas": arestas,
            "entrada": grafo.entrada,
            "saida": grafo.saida,
            "incidente": grafo.incidente,
            "pos": pos
        }

        with open(caminho_arquivo, 'w') as f:
            json.dump(salvar_dados, f, indent=4)

    def carregar(self, caminho_arquivo):
        with open(caminho_arquivo, 'r') as f:
            dados = json.load(f)

        grafo = Grafo()

        # Adiciona nós
        for no in dados.get("nos", []):
            grafo.adicionar_no(no)

        # Adiciona arestas com pesos
        for aresta in dados.get("arestas", []):
            origem = aresta.get("origem")
            destino = aresta.get("destino")
            peso = aresta.get("peso", 1.0)
            if origem and destino:
                grafo.adicionar_aresta(origem, destino, peso)

        # Atribui entrada, saída e incidente
        grafo.entrada = dados.get("entrada")
        grafo.saida = dados.get("saida")
        grafo.incidente = dados.get("incidente")

        # Carrega layout fixo se existir
        pos = dados.get("pos")
        if pos:
            grafo.layout_fixo = {k: tuple(v) for k, v in pos.items()}
        else:
            grafo.layout_fixo = None

        return grafo
