for i in range(10):
    
    if i == 2:
        print('O 2 foi pulado')
        continue

    if i == 8:
        print('Chegou no 8, não chegara no else')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For finalizado com sucesso.')
