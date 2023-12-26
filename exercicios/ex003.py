num1 = input('Digite um valor: ')
num2 = input('Digite outro valor: ')

valor1 = int(num1)
valor2 = int(num2)
if num1 > num2:
  print(f'O primeiro valor: {valor1} é maior que o segundo valor: {valor2} ')
elif num1 == num2:
  print(f'Os valores digitados são iguais')
else:
  print(f'O segundo valor: {valor2} é maior que o primeiro valor: {valor1} ')