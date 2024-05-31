# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

listar = []
desfazer = []
refazer = []

while True:
    tarefas = input(
        'Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ').lower()
    print()
    if tarefas == 'desfazer' and listar == []:
        print('Nada à desfazer.')
        print()
        continue

    if tarefas == 'refazer' and desfazer == []:
        print('Nada à refazer.')
        print()
        continue

    print('Tarefas:')

    listar.append(tarefas)

    if tarefas == 'refazer':
        refazer.append(desfazer[-1])
        listar.pop()
        listar.append(refazer[-1])

    if tarefas == 'desfazer':
        desfazer.append(listar[-2])
        listar.pop()
        listar.pop()

    if tarefas == 'listar':
        listar.pop()
        for itens in listar:
            print(itens)

    if tarefas == 'clear':
        os.system('cls')
        listar.pop()

    print()
