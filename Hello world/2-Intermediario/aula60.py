# Problemas dos parâmetros mutáveis em funções python
def adicionar_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


clientes1 = adicionar_clientes('Lucas')
adicionar_clientes('Tiago', clientes1)
clientes1.append('Joilma')
print(clientes1)
clientes2 = adicionar_clientes('Ana Júlia')
adicionar_clientes('Joaquim', clientes2)
clientes2.append('Adriano')
print(clientes2)
