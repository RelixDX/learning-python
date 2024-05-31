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
import copy

d1 = {
    'nome': 'Lucas',
    'sobrenome': 'Souza',
    'idade': 20,
    'endereço': ['ARA ARA', 10]
}

# d2 = copy.deepcopy(d1)
d2 = d1.copy()

d2['sobrenome'] = 'Oliveira'
d2['endereço'][1] = 0

print(d1)
print(d2)
