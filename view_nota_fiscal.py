# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
# Criando a Janela da Nota Fiscal
class View_Nota_Fiscal(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        #self.geometry('350x350+200+200')
        self.title('Nota Fiscal')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.lb_cliente = Label(self, text='Cliente: ')
        self.lb_vendedor = Label(self, text='Vendedor: ')
        self.lb_carro = Label(self, text='Carro Vendido: ')
        self.lb_preco_original = Label(self, text='Preço Original: ')
        self.lb_desconto = Label(self, text='Desconto: ')
        self.lb_preco_final = Label(self, text='Data de Venda: ')
        self.lb_forma_pagamento = Label(self, text='Forma de Pagamento: ')
        # Posicionando os widgets
        self.lb_cliente.grid(row=0, column=0)
        self.lb_vendedor.grid(row=1, column=0)
        self.lb_carro.grid(row=2, column=0)
        self.lb_preco_original.grid(row=3, column=0)
        self.lb_desconto.grid(row=4, column=0)
        self.lb_preco_final.grid(row=5, column=0)
        self.lb_forma_pagamento.grid(row=6, column=0)
    '''
    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()
    '''
    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

