soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        count = count + 1
print('A soma de todos os {} valores solicitados é de {}'.format(count, soma))
