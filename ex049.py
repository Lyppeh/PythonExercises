n = int(input('Digite o número que você deseja saber a tabuada: '))
print('=-' * 10)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('=-' * 10)
