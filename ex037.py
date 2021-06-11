num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Escolha uma opção '))
if opçao == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('{}OPÇÃO INVALIDA'.format('\033[1:31m'))
