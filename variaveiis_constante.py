

veloc_atual_carro = 60
localizacao_km_carro  = 90


VEL_RADAR_1_KM_hora = 60
LOCAL_Radar1_ESTA = 100

RADAR_RANGE_ALCANCE = 1

if veloc_atual_carro <= VEL_RADAR_1_KM_hora:
  print(f'Sua velocidade atual é {veloc_atual_carro}KM hora e esta dentro do permitido {VEL_RADAR_1_KM_hora}KM/H no Radar_1')
else:
  print('Voce esta acima da velocidade, e esta Multado!!')