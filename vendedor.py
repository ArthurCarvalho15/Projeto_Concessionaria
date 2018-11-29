# Importando a classe mãe Pessoa
from pessoa import Pessoa

# Classe Funcionário
class Vendedor(Pessoa):
    # Método Construtor
    def __init__(self, nome, idade, cpf, matricula, salario):
        # Atributos da classe mãe
        super().__init__(nome, idade, cpf)
        # Atributos próprios
        self.matricula = matricula
        self.salario = salario

    # Métodos get próprios
    def get_matricula(self):
        return self.matricula
    def get_salario(self):
        return self.salario

    # Método para converter a classe em um texto(string)
    def to_string(self):
        return self.nome + ';' + self.idade + ';' + self.cpf + ';' + self.matricula + ';' + str(self.salario)

    # Método para registrar os Vendedores na lista
    def registrar_lista(self):
        pass