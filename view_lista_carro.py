# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox

# Criando a Janela do Menu de Clientes
class View_Lista_Carro(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('350x350+200+200')
        self.title('Lista de Carros')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.lb_nome = Label(self, text='Nome')
        self.lb_marca = Label(self, text='Marca')
        self.lb_placa = Label(self, text='Placa')
        self.lb_ano_lancamento = Label(self, text='Ano de Lançamento')
        self.lb_estado = Label(self, text='Estado')
        self.lb_preco = Label(self, text='Preço')

        # Posicionando os widgets
        self.lb_nome.grid(row=0,column=0)
        self.lb_marca.grid(row=0, column=1)
        self.lb_placa.grid(row=0, column=2)
        self.lb_ano_lancamento.grid(row=0, column=3)
        self.lb_estado.grid(row=0, column=4)
        self.lb_preco.grid(row=0, column=4)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

