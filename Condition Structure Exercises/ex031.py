distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes acomeçar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem seá de R${:.2f}.'.format(preço))
