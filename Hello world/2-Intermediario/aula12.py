# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Lucas'
pessoa['sobrenome'] = 'Souza'

print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('Não existe.')
else:
    print(pessoa['sobrenome'])
