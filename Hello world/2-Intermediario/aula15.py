# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Souza',
    'idade': 20
}

# print(pessoa.get('nome'))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)
# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)
# pessoa.update({
#     'nome': 'Tiago',
#     'altura': 1.69
# })
# pessoa.update(nome='Tiago', altura=1.69)
# tupla = ('nome', 'Tiago'), ('altura', 1.69)
lista = [['nome', 'Tiago'], ['altura', 1.69]]
# pessoa.update(tupla)
pessoa.update(lista)
print(pessoa)
