"""
Higher order function
Função de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Boa Noite', 'Lucas'))
print(executa(saudacao, 'Boa Noite', 'Tiago'))
print(executa(saudacao, 'Boa Noite', 'Ana Julia'))
