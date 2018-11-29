# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
from cadastrar_cliente import Cadastrar_Cliente
from view_lista_cliente import View_Lista_Cliente

# Criando a Janela do Menu de Clientes
class Menu_Clientes(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('350x350+200+200')
        self.title('Menu de Clientes')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.btn_exit = Button(self, width=10,
                               text='Sair',
                               command=self.destroy)
        self.btn_lista = Button(self, width= 17,
                                text='Ver Lista de Clientes',
                                command= self.btn_lista_click)
        self.btn_add_cliente = Button(self, width= 15,
                                      text= 'Cadastrar Cliente',
                                      command= self.btn_add_cliente_click)
        # Posicionando os Widgets
        self.btn_exit.place(x=15, y=300)
        self.btn_lista.place(x=20, y=100)
        self.btn_add_cliente.place(x=20, y=150)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Método para abrir o Cadastro de Clientes
    def btn_add_cliente_click(self):
        Cadastrar_Cliente(self)

    # Método para abrir a Janela com a Lista de Clientes
    def btn_lista_click(self):
        View_Lista_Cliente(self)