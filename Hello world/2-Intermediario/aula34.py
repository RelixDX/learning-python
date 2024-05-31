# Try, Except, else e finally
try:
    print('Abriu arquivo')
    8/0
except ZeroDivisionError:
    print('Dividiu por zero.')
else:
    print('Não ocorreu nenhum erro.')
finally:
    print('Fechou arquivo')
