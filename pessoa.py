# Classe Mãe Pessoa
class Pessoa():
    # Método construtor
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    # Métodos get
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_cpf(self):
        return self.cpf
