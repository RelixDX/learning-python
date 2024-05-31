"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

acima_da_velocidade = velocidade > RADAR_1
carro_pass_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_pass_radar and acima_da_velocidade

if acima_da_velocidade:
    print('O carro está acima da velocidade permitida')
else:
    print('O carro está dentro da velocidade permitida')

if carro_multado:
    print('Perdeu')
else:
    print('ta safe')