#And -> todas as condicoes devem ser verdades

entrada = input('Digite [E]ntrar [S]air: ')
senha = input('Digite sua Senha:')

senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida:
  print('Acesspo permitido')
else:
  print('Acesso negado')
