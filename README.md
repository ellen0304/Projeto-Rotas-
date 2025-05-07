# RS - Rota Segura

🧭 **RS - Rota Segura** é um sistema desenvolvido em Python com interface gráfica (Tkinter) que auxilia a equipe de treinamento de emergência da universidade a simular e planejar rotas de evacuação em caso de incidentes como incêndios. O sistema utiliza algoritmos de grafos para encontrar a rota mais rápida (BFS) e rotas alternativas (DFS).

## 🚀 Funcionalidades

- Modelagem dinâmica do grafo (cada nó representa salas, portas, escadas, etc).
- Marcação do ponto de entrada, saída e local do incidente.
- Cálculo da rota mais curta com **BFS**.
- Geração de rotas alternativas com **DFS**.
- Visualização gráfica do mapa e dos caminhos encontrados.
- Exibição textual da sequência de nós da rota.
- Salvamento e reconsulta de simulações anteriores.

## 🖥️ Como Executar

1. Clone ou baixe este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Execute o sistema:
4. 
python main.py


🗃️ Estrutura de Pastas
📁rota_segura/
│
├── main.py                 # Arquivo principal para iniciar a aplicação
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
├── gui/                      # Arquivos relacionados à interface gráfica
│   └── app.py               # Implementação da interface gráfica com Tkinter
├── core/                     # Lógica do sistema
│   ├── grafo.py             # Manipulação do grafo e algoritmos de busca (BFS, DFS)
│   └── simulacao.py         # Lógica de simulação e salvamento de dados
├── data/                     # Dados do sistema
    └── simulações_salvas.json  # Arquivo JSON que armazena simulações de rotas


🛠️ Tecnologias Utilizadas

Python 3.13.3

Tkinter

NetworkX

Matplotlib


