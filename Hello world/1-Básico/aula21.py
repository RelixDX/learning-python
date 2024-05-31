# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda expressão como verdadeira.
# se qualquer valor for considerada verdadeiro,
# a expressão inteira vai ser avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]Entrar ou [S]Sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrou')
elif (entrada == 'S' or 's'):
    print('Saiu')
else:
    print('Digite [E] ou [S]')