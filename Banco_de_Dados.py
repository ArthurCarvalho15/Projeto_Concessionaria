# Criando o Banco de Dados
class Banco_de_Dados():
    # Método Construtor
    def __init__(self):
        # Atributos
        self.lista_carros = []
        self.lista_clientes = []
        self.lista_vendedores = []
        self.file_carros = []
        self.file_clientes = []
        self.file_clientes = []

    # Métodos get
    def get_lista_carros(self):
        return self.lista_carros
    def get_lista_clientes(self):
        return self.lista_clientes
    def get_lista_vendedores(self):
        return self.lista_vendedores

    # Método para carregar as listas
    '''
    1. Abrir os arquivos das listas 
    2. Separar os atributos de cada item com ; [split(';')]
        2.1 Cada linha deve ser um item 
    3. Inserir o objeto na lista de compras
    '''
    def load_lista_carros(self):
        pass
    def load_lista_clientes(self):
        pass
    def load_lista_vendedores(self):
        pass

    # Método para gravar as listas em seus respectivos arquivos
    '''
    1. Abrir os aquivos das listas
    2. Percorrer as listas (for item in lista: )
    3. Pra cada item, converter em string (item.to_string())
    4. Salvar nos arquivos
    '''
    def save_lista_carros(self):
        pass
    def save_lista_clientes(self):
        pass
    def save_lista_vendedores(self):
        pass
