# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
from carro import Carro

# Criando a Janela do Menu de Cadastro de Carros
class Cadastar_Carro(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('400x400+100+200')
        self.title('Cadastro de Carro')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.btn_exit = Button(self, width=10,
                               text='Sair',
                               command=self.destroy)
        self.entry_nome = Entry(self)
        self.lb_nome = Label(self, text='Nome: ',
                             bg='light blue')
        self.entry_marca = Entry(self)
        self.lb_marca = Label(self, text='Marca: ',
                              bg='light blue')
        self.entry_placa = Entry(self)
        self.lb_placa = Label(self, text='Placa: ',
                              bg='light blue')
        self.entry_ano_lancamento = Entry(self)
        self.lb_ano_lancamento = Label(self, text='Ano de Lançamento: ',
                                       bg='light blue')
        self.entry_estado = Entry(self)
        self.lb_estado = Label(self, text='Estado: ',
                               bg='light blue')
        self.entry_preco = Entry(self)
        self.lb_preco = Label(self, text='Preço: ',
                              bg='light blue')
        self.btn_register = Button(self, width=15,
                                   text='Adcionar Carro',
                                   command= self.register_carro)

        # Posicionando os Widgets
        self.entry_nome.place(x=97, y=100)
        self.lb_nome.place(x=50, y=100)
        self.entry_marca.place(x=95, y=130)
        self.lb_marca.place(x=50, y=130)
        self.entry_placa.place(x=94, y=160)
        self.lb_placa.place(x=50, y=160)
        self.entry_ano_lancamento.place(x=170, y=190)
        self.lb_ano_lancamento.place(x=50, y=190)
        self.entry_estado.place(x=100, y=220)
        self.lb_estado.place(x=50, y=220)
        self.entry_preco.place(x=100, y=250)
        self.lb_preco.place(x=50, y=250)
        self.btn_exit.place(x=15, y=350)
        self.btn_register.place(x=270, y=350)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Método para registrar o carro
    def register_carro(self):
        carro = Carro(self.entry_nome.get(), self.entry_marca.get(), self.entry_placa.get(),
              self.entry_ano_lancamento.get(), self.entry_estado.get(),
              self.entry_preco.get())
        lista = open('lista_carros', 'a')
        lista.write(f'{carro.to_string()}\n')
        messagebox.showinfo('Cadastro Realizado', 'Carro Registrado com sucesso!!')
        super().destroy()

'''
Nota: Use essa classe como base pra criar o cadastro dos carros, clientes e vendedores
'''