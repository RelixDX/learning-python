import pprint

# Mapeamento de dados em list comprehension


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 30, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 20, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] * 1.05) > 10
]

# print(*novos_produtos, sep='\n')
p(novos_produtos)
# lista = [n for n in range(10) if n >= 5]
# print(lista)
