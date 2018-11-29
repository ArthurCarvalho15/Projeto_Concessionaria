# Importando a janela
from janela_inicial import Janela

# Criando a classe de Controle
class Controle():
    # Método contrutor
    def __init__(self):
        # Atributos
        self.jnl = Janela(self)
        self.jnl.mainloop() #Deixar a janela ativa


