#And -> Ao menos uma das condicoes devem ser verdades

entrada = input('Digite [E]ntrar [S]air: ')
senha = input('Digite sua Senha:')

senha_permitida = '123456'

if( entrada == 'E' or 'e') or senha == senha_permitida:
  print('Acesso permitido')
else:
  print('Acesso negado')
