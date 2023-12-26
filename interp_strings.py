"""
Interpolacao basica de strings

s -> strings
d e i -> int
f -> float

x X -> hexadecimal(ABCDEF0123456789)

"""

# nome = 'sivaldo'
# preco = 100.9876543

# variavel = '%s, o preco é R$%.2f' %(nome, preco)
# print(variavel)

# print('O hexadecimal de %d é %04x' % (15, 15))
# print('O hexadecimal de %d é %04x' % (150, 150))
# print('O hexadecimal de %d é %04x' % (1500, 1500))


variavel = 'ABC'

print(f' {variavel} ')
print(f' {variavel: >10}')
print(f' {variavel: <10} {variavel}')
print(f' {variavel: ^10}. ')

print(f'{100.2345678:.1f}')



#fatiamento de strings

variavel = 'Ola mundo'
print(variavel[2:5])
print(variavel[0:5])
print(variavel[0:8])
print(variavel[0:10])
print(variavel[0:])
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(len(variavel))
print(variavel[0:9:2])
