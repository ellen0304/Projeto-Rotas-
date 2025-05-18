from gui.app import App
from rotas import grafo, dijkstra, caminho_mais_curto

if __name__ == "__main__":
    app = App()
    app.mainloop()

inicio = "Biblioteca"
destino = "Saída"

distancias, anteriores = dijkstra(grafo, inicio)
caminho = caminho_mais_curto(anteriores, destino)

print(f"Menor caminho de {inicio} até {destino}: {' -> '.join(caminho)}")
print(f"Distância total: {distancias[destino]}")