"""
Cuidado com os mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutáveis)
"""
lista_a = ['Lucas', 'Tiago', 1, True, 2.5]
lista_b = lista_a.copy()

lista_a[0] = 'Eu mesmo'
print(lista_b, lista_a)