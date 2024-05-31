# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está ligando', self.phone)
        return 2341


call1 = CallMe('22905225933')
retorno = call1('Lucas')
print(retorno)
