"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_aleatorio = input('Digite um número inteiro: ')

# try:
#     num_int = int(numero_aleatorio)
#     if (num_int % 2) == 0:
#         print(f'{num_int} é par')
#     else:
#         print(f'{num_int} é ímpar')
# except:
#     print('Informe um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Digite uma hora: ')


# try:
#     hora_int = int(hora)

#     bom_dia = hora_int >= 0 and hora_int <= 11
#     boa_tarde = hora_int >= 12 and hora_int <= 17
#     boa_noite = hora_int >= 18 and hora_int <= 23

#     if bom_dia:
#         print('Bom dia')
#     elif boa_tarde:
#         print('Boa tarde')
#     elif boa_noite:
#         print('Boa noite')
#     else:
#         print('Pedi a HORA')
# except:
#     print('Por favor digite um número.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# first_name = input('Digite seu primeiro nome: ')
# name_length = len(first_name)

# if name_length >= 2 and name_length <= 4:
#     print('Seu nome é curto')
# elif name_length >= 5 and name_length <= 6:
#     print('Seu nome é normal')
# elif name_length >= 7:
#     print('Seu nome é muito grande')
# else:
#     print('Digite dois caracteres ou mais.')