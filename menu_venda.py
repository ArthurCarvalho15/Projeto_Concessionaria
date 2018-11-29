# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
from venda import Venda
from view_nota_fiscal import View_Nota_Fiscal

# Criando a Janela do Menu de Venda
class Menu_Venda(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('400x400+100+200')
        self.title('Menu de Venda')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.btn_exit = Button(self, width=10,
                               text='Sair',
                               command=self.destroy)
        self.entry_cliente = Entry(self)
        self.lb_cliente = Label(self, text='Cliente: ',
                                bg='light blue')
        self.entry_vendedor = Entry(self)
        self.lb_vendedor = Label(self, text='Vendedor: ',
                                 bg='light blue')
        self.entry_carro = Entry(self)
        self.lb_carro = Label(self, text='Carro: ',
                              bg='light blue')
        self.entry_desconto = Entry(self)
        self.lb_desconto = Label(self, text='Desconto: ',
                                 bg='light blue')
        self.entry_preco = Entry(self)
        self.lb_preco = Label(self, text='Preço Original: ',
                                        bg='light blue')
        self.entry_forma_pagamento = Entry(self)
        self.lb_forma_pagamento = Label(self, text='Forma de Pagamento: ',
                                        bg='light blue')
        self.entry_data = Entry(self)
        self.lb_data = Label(self, text='Data da Venda: ',
                             bg='light blue')
        self.btn_register = Button(self, width=15,
                                   text='Registrar Venda',
                                   command= self.register_venda)

        # Posicionando os Widgets
        self.entry_cliente.place(x=100, y=100)
        self.lb_cliente.place(x=50, y=100)
        self.entry_vendedor.place(x=114, y=130)
        self.lb_vendedor.place(x=50, y=130)
        self.entry_carro.place(x=94, y=160)
        self.lb_carro.place(x=50, y=160)
        self.entry_preco.place(x=140, y=280)
        self.lb_preco.place(x=50, y=280)
        self.entry_desconto.place(x=114, y=190)
        self.lb_desconto.place(x=50, y=190)
        self.entry_forma_pagamento.place(x=176, y=220)
        self.lb_forma_pagamento.place(x=50, y=220)
        self.entry_data.place(x=140, y=250)
        self.lb_data.place(x=50, y=250)
        self.btn_exit.place(x=15, y=350)
        self.btn_register.place(x=270, y=350)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Método para registrar a venda no aquivo txt
    def register_venda(self):
        venda = Venda(self.entry_cliente.get(), self.entry_vendedor.get(), self.entry_carro.get(),self.entry_desconto.get(), self.entry_preco.get(), self.entry_data.get(), self.entry_forma_pagamento.get())
        lista = open('lista_venda', 'a')
        lista.write(f'{venda.to_string()}\n')
        View_Nota_Fiscal(self)
        messagebox.showinfo('Venda Registrada', 'Venda Registrada com Sucesso!!!')
        #super().destroy()


'''
Nota: Use essa classe como base pra criar o cadastro dos carros, clientes e vendedores
'''