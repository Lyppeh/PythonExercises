from datetime import  date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano {}º pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade < 18:
        totalmenor += 1
    else:
        totalmaior += 1
print('Ao todo tivemos {} pessoas menores de idade'.format(totalmenor))
print('Ao todo tivemos {} pessoas de maiores de idade'.format(totalmaior))

