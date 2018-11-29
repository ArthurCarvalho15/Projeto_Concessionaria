'''
=== Testes ===

# Importando bibliotecas
from janela import Janela

jnl = Janela()

# Colocando o título da janela principal
jnl.title("X Motors")
# Mudando a cor do background da janela
jnl['bg'] = 'light blue'
# Definindo as dimensões da janela

L = Largura 
A = Altura
E = Direção aonde será criada a janela partindo do canto esquerdo da tela do computador
T = Direção aonde será criada a janela partindo do canto superior(Topo) da tela do computador

jnl.geometry('L x A + E + T')

jnl.geometry('300x300+100+100')
jnl.mainloop()
'''
# Importando a Classe de Controle
from controle import Controle

Controle()
