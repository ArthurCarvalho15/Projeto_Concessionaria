# Importandos as bibliotecas
from tkinter import *
from tkinter import messagebox

# Criando a Janela do Menu de Clientes
class View_Lista_Cliente(Toplevel):
    # Metodo Construtor
    def __init__(self, parent):
        # Chamar o __init__() da classe mãe
        super().__init__(parent)
        # Atributos
        self.geometry('350x350+200+200')
        self.title('Lista de Clientes')
        self['bg'] = 'light blue'
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.lb_nome = Label(self, text='Nome')
        self.lb_idade = Label(self, text='Idade')
        self.lb_cpf = Label(self, text='CPF')

        # Posicionando os widgets
        self.lb_nome.grid(row=0,column=0)
        self.lb_idade.grid(row=0, column=1)
        self.lb_cpf.grid(row=0, column=2)

    # Método para fechar a janela
    def destroy(self):
        if messagebox.askokcancel('Confirmação', 'Deseja fechar a janela?'):
            super().destroy()

    # Método para avisar que o programa ta incompleto
    def btn_no_function(self):
        messagebox.showwarning('AVISO', 'O Programa ainda não possui essa funcionalidade')

