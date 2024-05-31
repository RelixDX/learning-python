# Criando datas com módulo datatime
# datetime(ano, mês, dia)
# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
# from pytz import timezone

data = datetime.now()
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1711761200.667443))
# data_str_data = '2024-02-11 22:25:13'
# data_str_data = '11/02/2024'
# data_str_fmt = '%d/%m/%Y'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2024, 2, 11, 22, 25, 13, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
