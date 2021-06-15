soma = 0
count= 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        count = count + 1
print('Você informou {} números PARES e a soma deles é {}'.format(count, soma))
