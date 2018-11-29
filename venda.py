# Classe de Venda de Carros
class Venda():
    # Método contrutor
    def __init__(self, carro, cliente, vendedor, desconto,preco, data, forma_pagamento):
        self.carro = carro
        self.cliente = cliente
        self.vendedor = vendedor
        self.desconto = desconto
        self.preco = preco
        self.preco_final = float(self.preco) - ((float(self.preco) * float(self.desconto))/100)
        self.data = data
        self.forma_pagamento = forma_pagamento

    # Imprimir a nota fiscal
    def print_nota_fiscal(self):
        print('== Nota Fiscal ==\n\n'
              f'Cliente: {self.cliente}\n'
              f'Vendedor: {self.vendedor}\n'
              f'Carro vendido: {self.carro}\n'
              f'Preço Original: R${self.preco}\n'
              f'Desconto: {self.desconto}%\n'
              f'Preço Final: R${self.preco_final}\n'
              f'Data da Venda: {self.data}\n'
              f'Forma de Pagamento: {self.forma_pagamento}\n'
              '== // ==\n\n')

    # Método para converter a classe em texto (string)
    def to_string(self):
        return self.cliente + ';' + self.vendedor + ';' + self.carro + ';' \
                + str(self.preco) + ';' + str(self.desconto) + ';' \
               + str(self.preco_final) + ';' + self.data + ';' \
               + self.forma_pagamento