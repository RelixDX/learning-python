"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""

condicao = 0

while condicao < 1000:
    condicao += 1

    if condicao == 40:
        continue

    print(condicao)

    if condicao == 50:
        break

print('Acabou!')