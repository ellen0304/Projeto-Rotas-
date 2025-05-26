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

## 🗃️ Estrutura de Pastas

Abaixo está a organização dos arquivos e diretórios do projeto **Rota Segura**:

📁 rota_segura/
│
├── main.py # Arquivo principal para iniciar a aplicação
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
│
├── gui/ # Tudo relacionado à interface Tkinter
│ └── app.py # Classe App (Tkinter)
│ └── componentes.py # Componentes auxiliares (ex: pop-ups)
│
├── core/ # Lógica do grafo e algoritmos
│ └── grafo.py # Classe Grafo com métodos BFS, DFS e modificações
│ └── simulacao.py # Gerenciamento de simulações salvas
│
├── data/ # Arquivos de simulações salvas (JSON)



🛠️ Tecnologias Utilizadas

Python 3.x

Tkinter
<img width="960" alt="tela-inicial-rs" src="https://github.com/user-attachments/assets/b98f5bb0-68d1-403f-86d3-7365f7054551" />

NetworkX

Matplotlib


## 🖥️ Como Executar

1. Clone ou baixe este repositório.

2. 📦 Criando e ativando um ambiente virtual (venv) em Python

Siga os passos abaixo para criar e ativar um ambiente virtual com Python.

Acesse a pasta do seu projeto

```bash
cd caminho/da/sua/pasta
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt 

4. Execute o sistema:
```bash
python main.py



