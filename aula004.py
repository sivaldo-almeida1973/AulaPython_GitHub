"""
Conversão de tipos , coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro

Tipos imutaveis e primitivos:
#str, int , float, bool

"""
# print(1+1)
# print('a'+'b') #concatenação

#-------------------------------------
#print('1'+ 1) #type error
#print('a'+ 1) #type error


print(int('1'), type(int('1')))

print(int('1')+ 1)
print(float('1')+ 1)

print(bool(' '))

#print(11 + 'n')#TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(str(11) + 'n')