n1 = float(input('Qual a nota da primeira prova: '))
n2 = float(input('E qual a nota da segunda prova: '))
media = (n1 + n2) / 2
print('A sua média foi de {} pontos'.format(media))
if media < 5:
    print('{}REPROVADO!{}'.format('\033[1:31m', '\033[m'))
elif media >= 5 and media < 7:
    print('{}RECUPERAÇÃO{}'.format('\033[1:33m', '\033[m'))
else:
    print('{}APROVADO{}'.format('\033[1:32m' , '\033[m'))
