# Imporatando a classe mãe Pessoa
from pessoa import Pessoa

# Criando a Classe Cliente
class Cliente(Pessoa):
    # Método Contrutivo
    def __init__(self, nome, idade, cpf):
        # Atributos da classe mãe
        super().__init__(nome, idade, cpf)

    # Método para converter a classe em um texto(string)
    def to_string(self):
        return self.nome + ';'+ self.idade + ';'+ self.cpf

    # Método para registrar os clientes na lista
    def registrar_lista(self):
         pass