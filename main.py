# Importa a classe InterfaceGrafica do arquivo interface.py
from interface import InterfaceGrafica

# Verifica se este arquivo é o principal (o ponto de entrada)
if __name__ == "__main__":
    # Cria uma instância da InterfaceGrafica e inicia o aplicativo
    app = InterfaceGrafica()
    app.mainloop()  # Inicia o loop da interface gráfica
