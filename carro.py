# Classe  Carro
class Carro():
    # Método Construtor
    def __init__(self, nome, marca, placa, ano_lancamento, estado, preco):
        self.nome = nome
        self.marca = marca
        self.placa = placa
        self.ano_lancamento = ano_lancamento
        self.estado = estado
        self.preco = preco

    # Métodos get
    def get_nome(self):
        return self.nome
    def get_marca(self):
        return self.marca
    def get_placa(self):
        return self.placa
    def get_ano_lancamento(self):
        return self.ano_lancamento
    def get_estado(self):
        return self.estado
    def get_preco(self):
        return self.preco

    # Método para converter a classe em texto (string)
    def to_string(self):
        return self.nome + ';' + self.marca + ';' + self.placa + ';' \
               + self.ano_lancamento + ';' + self.estado + ';' + self.preco