# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox
from cadastrar_vendedor import Cadastrar_Vendedor
from view_lista_vendedor import View_Lista_Vendedor

# Criando a Janela do Menu
class Menu_Vendedor(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('350x350+200+200')
        self.title('Menu de Vendedores')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.btn_exit = Button(self, width=10,
                               text='Sair',
                               command=self.destroy)
        self.btn_lista = Button(self, width= 19,
                                text='Ver Lista de Vendedores',
                                command= self.btn_lista_click)
        self.btn_add_vendedor = Button(self, width= 15,
                                       text='Cadastrar Vendedor',
                                       command= self.btn_add_vendedor_click)
        # Posicionando os Widgets
        self.btn_exit.place(x=15, y=300)
        self.btn_lista.place(x=20, y=100)
        self.btn_add_vendedor.place(x=20, y=150)

    '''
    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()
    '''

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Método para abrir o Cadastro de Vendedores
    def btn_add_vendedor_click(self):
        Cadastrar_Vendedor(self)

    # Método para ver a lista de Vendedores
    def btn_lista_click(self):
        View_Lista_Vendedor(self)