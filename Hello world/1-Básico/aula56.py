"""
Faça uma lista de comprar com lista
o usuário deve ter possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
compras = []

while True:
    try:
        print('Selecione uma Opção')
        opcoes = input('[i]nserir [a]pagar [l]istar: ').lower()

        if opcoes == 'i':
            compra = input('Item: ')
            compras.append(compra)
            continue

        try:
            if opcoes == 'a':
                apagar = input('Digite o índice do que deseja apagar: ')
                apagar_int = int(apagar)
                compras.remove(compras[apagar_int])
                continue
        except:
            print('Digite um índice existente.')

        if opcoes == 'l':
            for indice, compra in enumerate(compras):
                print(indice, compra)
            if compras == []:
                print('Não tem compras existentes.')

        if opcoes == 's':
            break
    except:
        print('Selecione uma opção valida')
        continue