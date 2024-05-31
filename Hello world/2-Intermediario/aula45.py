# Decoradores com parâmetros
def decorators_factory(a=None, b=None, c=None):
    def function_factory(func):
        print('Decoradora 1')

        def aninhada(*arg, **kwarg):
            print('Aninhada')
            res = func(*arg, **kwarg)
            return res
        return aninhada
    return function_factory


@decorators_factory(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = decorators_factory()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
