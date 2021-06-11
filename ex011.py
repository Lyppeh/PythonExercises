lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar*alt
print('Sua parede tem as dimensoes de {}m x {}m e sua area tem {:.2f}m²'.format(lar, alt, area))
tinta = area / 2
print('Para pintar sua parede você precisa de {}l de tinta'.format(tinta))


