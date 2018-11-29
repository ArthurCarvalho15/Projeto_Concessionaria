# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
from vendedor import Vendedor

# Criando a Janela do Menu
class Cadastrar_Vendedor(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('400x400+100+200')
        self.title('Cadastro de Vendedor')
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
        self.entry_matricula = Entry(self)
        self.lb_matricula = Label(self, text='Matrícula: ',
                                  bg='light blue')
        self.entry_salario = Entry(self)
        self.lb_salario = Label(self, text='Salario: ',
                                bg='light blue')
        self.btn_register = Button(self, width=15,
                                   text='Cadastrar Vendedor',
                                   command= self.register_vendedor)

        # Posicionando os Widgets
        self.entry_nome.place(x=100, y=100)
        self.lb_nome.place(x=50, y=100)
        self.entry_idade.place(x=95, y=130)
        self.lb_idade.place(x=50, y=130)
        self.entry_cpf.place(x=94, y=160)
        self.lb_cpf.place(x=50, y=160)
        self.entry_matricula.place(x=114, y=190)
        self.lb_matricula.place(x=50, y=190)
        self.entry_salario.place(x=100, y=220)
        self.lb_salario.place(x=50, y=220)
        self.btn_exit.place(x=15, y=350)
        self.btn_register.place(x=270, y=350)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Método para registrar o vendedor
    def register_vendedor(self):
        vendedor = Vendedor(self.entry_nome.get(), self.entry_idade.get(),
                            self.entry_cpf.get(), self.entry_matricula.get(),
                            self.entry_salario.get())
        lista = open('lista_vendedores', 'a')
        lista.write(f'{vendedor.to_string()}\n')
        messagebox.showinfo('Cadastro Concluído', 'Cadastro Realizado com Sucesso')
        super().destroy()

'''
Nota: Use essa classe como base pra criar o cadastro dos carros, clientes e vendedores
'''