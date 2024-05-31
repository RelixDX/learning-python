# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# while True:
#     def pergunta_1():
#         print('Quanto é 2+2?')
#         print()
#         print('Opções:')
#         print('0) 1')
#         print('1) 3')
#         print('2) 4')
#         print('3) 5')

#         try:
#             resposta = int(input('Escolha uma opção: '))

#             if resposta == 2:
#                 resposta_correta = resposta

#             if perguntas[0]['Opções'][resposta_correta]:
#                 print('Acertou')
#         except:
#             print('Errou')

#     pergunta_1()

#     def pergunta_2():
#         print('Quanto é 5*5?')
#         print()
#         print('Opções:')
#         print('0) 25')
#         print('1) 55')
#         print('2) 10')
#         print('3) 51')

#         try:
#             resposta = int(input('Escolha uma opção: '))

#             if resposta == 0:
#                 resposta_correta = resposta

#             if perguntas[0]['Opções'][resposta_correta]:
#                 print('Acertou')
#         except:
#             print('Errou')

#     pergunta_2()

#     def pergunta_3():
#         print('Quanto é 10/2?')
#         print()
#         print('Opções:')
#         print('0) 4')
#         print('1) 5')
#         print('2) 2')
#         print('3) 1')

#         try:
#             resposta = int(input('Escolha uma opção: '))

#             if resposta == 1:
#                 resposta_correta = resposta

#             if perguntas[0]['Opções'][resposta_correta]:
#                 print('Acertou')
#         except:
#             print('Errou')

#     pergunta_3()

#     # print(f'Acertou {} de {} perguntas.')
#     break

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    print('Opções:')

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

    print()

print(f'Você acertou {qtd_acertos} respostas de {len(perguntas)} perguntas.')
