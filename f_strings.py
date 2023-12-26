nome = 'sivaldo'
altura = 1.7000
peso = 86
imc = peso / (altura ** 2)



resultado = f'{nome} tem {altura:.2f} de altura'
print('Resultado:',resultado)


print(f'Nome: {nome} Peso:{peso} Altura:{altura} e seu IMC:{imc:.2f}')


#format

a = 10
b = 11
c = 1.1

formato = 'a={} b={} c={}'.format(a,b,c)
print(formato)