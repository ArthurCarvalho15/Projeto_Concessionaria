# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
from cliente import Cliente

# Criando a Janela do Menu
class Cadastrar_Cliente(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('400x400+100+200')
        self.title('Cadastro de Cliente')
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
        self.entry_idade = Entry(self)
        self.lb_idade = Label(self, text='Idade: ',
                            bg='light blue')
        self.entry_cpf = Entry(self)
        self.lb_cpf = Label(self, text='CPF: ',
                            bg='light blue')
        self.btn_register = Button(self, width=15,
                                   text='Cadastrar Cliente',
                                   command= self.register_cliente)

        # Posicionando os Widgets
        self.entry_nome.place(x=95, y=100)
        self.lb_nome.place(x=50, y=100)
        self.entry_idade.place(x=94, y=130)
        self.lb_idade.place(x=50, y=130)
        self.entry_cpf.place(x=94, y=160)
        self.lb_cpf.place(x=50, y=160)
        self.btn_exit.place(x=15, y=350)
        self.btn_register.place(x=270, y=350)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Método para registrar o cliente
    def register_cliente(self):
        cliente = Cliente(self.entry_nome.get(), self.entry_idade.get(), self.entry_cpf.get())
        lista = open('lista_clientes', 'a')
        lista.write(f'{cliente.to_string()}\n')
        messagebox.showinfo('Cadastro Concluido', 'Cadastro Realizado com Sucesso!!')
        super().destroy()

'''
Nota: Use essa classe como base pra criar o cadastro dos carros, clientes e vendedores
'''