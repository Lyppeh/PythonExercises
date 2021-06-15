soma = 0
media = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = 0
mulheres_com_menos_de_20_anos = 0

for d in range(1, 5):
    print('----------- {} PESSOA ----------'.format(d))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [M/F]: ')).strip()
    soma += idade
    if d == 1 and sexo in 'Mm':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_com_menos_de_20_anos += 1

media = soma / 4
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('A idade do homem mais velho é de {} anos, e seu nome é {}'.format(idade_homem_mais_velho, nome_homem_mais_velho))
print('{} mulheres tem menos de 20 anos'.format(mulheres_com_menos_de_20_anos))
