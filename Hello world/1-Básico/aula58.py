"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = '     Olha só que    ,     coisa interessante     '
lista_crua = frase.split(',')

lista_frase = []
for i, frases in enumerate(lista_crua):
    lista_frase.append(lista_crua[i].strip())

# print(lista_crua)
# print(lista_frase)

frases_unidas = ' '.join(lista_frase)
print(frases_unidas)