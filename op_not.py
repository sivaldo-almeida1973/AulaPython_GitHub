#not -> usado par inverter expressoes

# entrada = input('Digite [E]ntrar [S]air: ')
# senha = input('Digite sua Senha:')

# senha_permitida = '123456'

# if( entrada != 'E' or 'e') or senha != senha_permitida:
#   print('Acesso permitido')
# else:
#   print('Acesso negado')



# print(not True)
# print(not False)


# senha = input('Senha: ')

# if senha != '1234':
#   print('senha incorreta')


#Op in e not in

# nome = 'sivaldo'

# print('a' in nome)
# print('a' not in nome)






nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} esta em {nome}')
else:
  print(f'{encontrar} não esta em {nome}')

