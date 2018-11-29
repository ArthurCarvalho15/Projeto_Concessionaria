# Importar a biblioteca do Tkinter e os Menus
from tkinter import *
from tkinter import messagebox
from menu_carros import Menu_Carros
from menu_cliente import Menu_Clientes
from menu_vendedor import Menu_Vendedor
from menu_venda import Menu_Venda

# Criando a Janela Inicial
# Tk = Instancia do Tkinter necessária para a criação da tela
class Janela(Tk):
   # Método Construtor
    def __init__(self, controle):
        # Atributos
        self.controle = controle
        # Inicialzidando o método da classe mãe (tkinter)
        super().__init__()
        # Colocando o tílulo da janela
        self.title('X Motors')
        # Definindo as dimensões da janela
        self.geometry('400x400+600+200')
        # Mudando a cor do background
        self['bg'] = 'light blue'

        # Widgets
        self.label_boas_vindas = Label(self, text='Bem vindo a X Motors!')
        self.label_boas_vindas['bg'] = 'light blue'
        self.label_options = Label(self, text='O que deseja fazer?')
        self.label_options['bg'] = 'light blue'
        # == Menu ==
        self.btn_acessar_carros = Button(self, width=15,
                                         text='Acessar Carros',
                                         command= self.btn_start_menu_carros)
        self.btn_acessar_clientes = Button(self, width=15,
                                           text='Acessar Clientes',
                                           command= self.btn_start_menu_clientes)
        self.btn_acessar_vendedores = Button(self, width=15,
                                             text='Acessar Vendedores',
                                             command= self.btn_start_menu_vendedores)
        self.btn_start_venda = Button(self, width=15,
                                      text= 'Realizar Venda',
                                      command=self.btn_start_menu_venda)
        '''
        self.bnt_start = Button(self, width= 10,
                                text='Começar',
                                command=self.btn_start_menu)
        '''
        self.btn_close = Button(self, width= 10,
                                text='Sair',
                                command=self.destroy)
        # Posicionando os widgets
        self.label_boas_vindas.place(x=140, y= 30)
        self.label_options.place(x=140, y=60)
        #self.bnt_start.place(x=140, y=200)
        self.btn_close.place(x=160,y=300)
        self.btn_acessar_carros.place(x=45, y=100)
        self.btn_acessar_clientes.place(x=45, y=200)
        self.btn_acessar_vendedores.place(x=250, y=200)
        self.btn_start_venda.place(x=250, y=100)

    # Método para destruir a janela
    def destroy(self):
        # Janela de Confirmação (menssagebox)
        if messagebox.askokcancel('Confirmação','Deseja sair?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

    # Métodos para criar os Menus
    def btn_start_menu_carros(self):
        Menu_Carros(self)
    def btn_start_menu_clientes(self):
        Menu_Clientes(self)
    def btn_start_menu_vendedores(self):
        Menu_Vendedor(self)
    def btn_start_menu_venda(self):
        Menu_Venda(self)