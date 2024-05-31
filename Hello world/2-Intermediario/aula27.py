# isinstace - para saber se o objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Lucas'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print('SET')
        print(item, isinstance(item, str))

    if isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))

    if isinstance(item, (int, float)):
        print('INT/FLOAT')
        print(item, isinstance(item, str))
