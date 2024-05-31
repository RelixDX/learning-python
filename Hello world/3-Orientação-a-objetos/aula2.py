# Método em instâncias de classes Python
# Hard Coded - Algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome_carro='algo'):
        self.nome = nome_carro

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
