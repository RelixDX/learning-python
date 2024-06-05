# Descobrir sua idade
from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y'

aniversario = str(input('Digite seu aniversaio: '))
hoje = datetime.today().date().__format__(fmt)

nascimento = datetime.strptime(aniversario, fmt)
ano_atual = datetime.strptime(hoje, fmt)

idade = relativedelta(ano_atual, nascimento)

print(f'Sua idade é de {idade.years} anos')
