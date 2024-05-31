# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Lucas', 'sobrenome': 'Souza',
# }

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.69
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyboard arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, 3, 4, nome='Lucas', sobrenome='Souza')
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)
