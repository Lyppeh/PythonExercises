n1 = int(input('Informe um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Analizando o número {}'.format(n1))
print('Unidade: {}'.format(u))
print('Dezesna: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}' .format(m))
