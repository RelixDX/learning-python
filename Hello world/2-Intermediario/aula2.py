"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""


def soma(x, y):
    # Definição
    print(f'{x=} {y=}','|','x + y =', x + y)

soma(1, 4)
soma(y=4, x=1)