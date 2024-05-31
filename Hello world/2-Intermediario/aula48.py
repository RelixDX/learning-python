"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# l1 = lista_a = [1, 2, 3, 4, 5, 6, 7]
# l2 = lista_b = [1, 2, 3, 4]

# menor = min(len(l1), len(l2))

# somando = list(zip(l1[:menor], l2[:menor]))
# lista_soma = []

# for tupla in somando:
#     resultado = tupla[0] + tupla[1]
#     lista_soma.append(resultado)

# print(lista_soma)

# -------------------------------------------------
# Outra solução

# l1 = lista_a = [1, 2, 3, 4, 5, 6, 7]
# l2 = lista_b = [1, 2, 3, 4]

# lista_soma = []
# for i in range(len(l2)):
#     lista_soma.append(l1[i] + l2[i])

# print(lista_soma)

# -----------------------------------------
# Outra solução

# l1 = lista_a = [1, 2, 3, 4, 5, 6, 7]
# l2 = lista_b = [1, 2, 3, 4]

# lista_soma = []
# for i, _ in enumerate(l2):
#     lista_soma.append(l1[i] + l2[i])

# print(lista_soma)

# ------------------------------------------
# Melhor solução (segundo o professor)

l1 = lista_a = [1, 2, 3, 4, 5, 6, 7]
l2 = lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(l1, l2)]

print(lista_soma)
