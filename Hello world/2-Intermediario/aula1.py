"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def python():
#     print('Olá')
#     print('Cheguei no intermediário')

# python()

# def python(a, b):
#     print(a, b)

# python(1, 2)

def nomes(nome='Sem nome'):
    print(f'Olá, {nome}!')

seu_nome = input('Qual seu nome? ')

if seu_nome:
    nomes(seu_nome)
else:
    print('Digite seu nome.')