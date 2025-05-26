# 🚀 RS – Rota Segura

**Resumo:** O RS – Rota Segura é um sistema interativo para simulação de rotas de evacuação em ambientes universitários, utilizando algoritmos de grafos. Através de uma interface gráfica intuitiva, o aplicativo permite o planejamento eficiente de rotas seguras considerando diferentes cenários, como incidentes ou bloqueios inesperados.

---

## 🎯 Objetivo

O projeto tem como objetivo principal auxiliar equipes de segurança e gestores na identificação de rotas de evacuação eficientes em situações de emergência. Utilizando conceitos de Teoria dos Grafos, o sistema modela ambientes como grafos e aplica os algoritmos de Dijkstra, BFS e DFS para calcular e comparar caminhos possíveis entre pontos de entrada e saída. A aplicação permite a visualização gráfica dessas rotas, a simulação de bloqueios e a análise da resiliência das opções disponíveis. Assim, o sistema promove um planejamento mais seguro e assertivo, unindo teoria computacional à prática em situações reais, alinhado aos conteúdos estudados na disciplina.

---

## 👨‍💻 Tecnologias Utilizadas

- Python 3.12
- Tkinter 
- Matplotlib 
- NetworkX 
- JSON


---

## 🗂️ Estrutura do Projeto

 
```
📦 nome-do-projeto
├── 📁 core
│   ├── grafo.py
│   └── simulacao.py
├── 📁 data
│   └── simulacoes-salvas/
├── 📁 gui
│   ├── app.py
│   ├── icone.ico
│   └── icone.png
├── README.md
├── main.py
└── requirements.txt
```

---

## ⚙️ Como Executar

### ✅ Rodando Localmente

1. Clone o repositório:

```
git clone https://github.com/ellen0304/Projeto-Rotas-
cd Projeto-Rotas-
```

2. Crie o ambiente virtual e ative:

```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
python main.py
```

---

## 📸 Demonstrações

- Tela inicial do sistema

<img width="960" alt="tela-inicial-rs" src="https://github.com/user-attachments/assets/a4f03bad-f7f1-412a-a6b1-66ee3654f1de" />

 
- Funcionalidade "Carregar simulação" (Aqui foi utilizado um mapa pré-salvo referente ao arquivo "mapa4.json" da pasta "data"

<img width="960" alt="funcao-carregar-simulacao" src="https://github.com/user-attachments/assets/9ba62cf8-9c2d-4215-aa7a-436877a18485" />


- Resultados esperados: Obter históricos de rotas encontradas nos 3 algoritmos (para comparação)

<img width="960" alt="resultado-esperado-rotas-comparativo" src="https://github.com/user-attachments/assets/b71f7a22-b725-4ab8-bc1c-9a4f9dfd0b18" />


---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Beatriz Courel | [@courelbeatriz](https://github.com/fulano) |
| Flávia de Souza | [@ellen0304](https://github.com/ellen0304) |
| Gabriele Antonio | [@Gabi160 ](https://github.com/Gabi160) |

---

## 🧠 Disciplinas Envolvidas

- Teoria dos Grafos

---

## 🏫 Informações Acadêmicas

- Universidade: **Universidade Braz Cubas**
- Curso: **Análise e Desenvolvimento de Sistemas**
- Semestre: 2º 
- Período: Noite
- Professora orientadora: **Dra. Andréa Ono Sakai**
- Evento: **Mostra de Tecnologia 1º Semestre de 2025**
- Local: Laboratório 12
- Datas: 05 e 06 de junho de 2025

---

## 📄 Licença

MIT License — sinta-se à vontade para utilizar, estudar e adaptar este projeto.
