# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')
    return True


def int_ou_float(n):
    type_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'{n} deve ser int ou float '
            f'"{type_n.__name__}" enviado.'
        )
    return True


def divide(n, d):

    int_ou_float(n)
    int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))
