

# num = input('Vou dobrar o numero uqe digitar:')
# dobro_num = float(num)
# if num.isdigit(): 
#   print(f'O dobro do numero{num} é igual:{dobro_num * 2}')
# else:
#   print('isso não é um numero!')


num = input('Vou dobrar o numero uqe digitar:')


try:
   dobro_num = float(num)
   print(f'O dobro do numero:{num} é igual:{dobro_num * 2}')
except:
  print('isso não é um numero!')