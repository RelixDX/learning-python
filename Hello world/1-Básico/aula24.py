"""

Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Lucas'
preco = 190.7141485
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)