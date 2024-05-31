# frase = 'O python é uma linguagem de programação ' \
#     'multiparadigma. ' \
#     'Python foi criada por Guido van Rossu.'

# i = 0
# apareceu_mais_vezes = 0
# letra_que_apareceu_mais = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     numero_de_vezes_letra_aparece = frase.count(letra_atual)

#     if apareceu_mais_vezes < numero_de_vezes_letra_aparece:
#         apareceu_mais_vezes = numero_de_vezes_letra_aparece
#         letra_que_apareceu_mais = letra_atual

#     i += 1

# print(f'A letra que apareceu mais vezes foi "{letra_que_apareceu_mais}"'
#     f' que apareceu {apareceu_mais_vezes}x'      
# )

frase = 'Tiago é um corno, feio e namorado de tamiris'

i = 0
qtd_vezes_apareceu = 0
qm_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_vezes_apareceu < qtd_letra_atual:
        qtd_vezes_apareceu = qtd_letra_atual
        qm_apareceu_mais = letra_atual

    i += 1

print(f'O "{qm_apareceu_mais}" apareceu {qtd_vezes_apareceu}x')