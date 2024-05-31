import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.1

print('Novos Valores')
for produto in novos_produtos:
    print(f"nome: {produto['nome']}, preco: {produto['preco']:.2f}")

print()
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)

print('Nome decrescente')
for produto in produtos_ordenados_por_nome:
    print(produto)
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x['preco'], reverse=False)

print('Preço crescente')
for produto in produtos_ordenados_por_preco:
    print(produto)
print()

# Original
print('Original')
print(*produtos, sep='\n')
