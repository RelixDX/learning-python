"""
Flag (Bandeira) - Marcar um local
none = Não valor
is e is not = é ou nao é (tipo, valor, indentidade)
id = identidade
"""

# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')