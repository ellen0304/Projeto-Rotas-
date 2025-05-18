import json

class SimulacaoManager:
    def salvar(self, filename, grafo):
        data = {
            "nos": list(grafo.grafo.nodes),
            "arestas": list(grafo.grafo.edges),
            "entrada": grafo.entrada,
            "saida": grafo.saida,
            "incidente": grafo.incidente
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def carregar(self, filename, grafo):
        with open(filename, "r") as f:
            data = json.load(f)
        grafo.grafo.clear()
        grafo.grafo.add_nodes_from(data["nos"])
        grafo.grafo.add_edges_from(data["arestas"])
        grafo.entrada = data.get("entrada")
        grafo.saida = data.get("saida")
        grafo.incidente = data.get("incidente")
