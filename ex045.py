from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('=-' * 20)
print('''SUAS OPÇÕES:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
print('=-' * 20)
jogador = int(input('Qual sua jogada? '))
computador = randint(1, 3)

if jogador != 1 and jogador != 2 and jogador != 3:
    print('{}JOGADA INVALIDA!{}, Escolha uma opção valida'.format('\033[1:31m', '\033[m'))
else:
    print('=-' * 15)
    print('O computador escolheu {}'.format(itens[computador]))
    print('o jogador escolheu {}'.format(itens[jogador]))
    print('=-' * 15)

    if computador == 1:
        if jogador == 1:
            print('{}EMPATE'.format('\033[1:33m'))
        elif jogador == 2:
            print('{}PARABÉNS! VOCÊ GANHOU'.format('\033[1:32m'))
        elif jogador == 3:
            print('{}VOCÊ PERDEU!'.format('\033[1:31m'))
    if computador == 2:
        if jogador == 1:
            print('{}VOCÊ PERDEU!'.format('\033[1:31m'))
        elif jogador == 2:
            print('{}EMPATE'.format('\033[1:33m'))
        elif jogador == 3:
            print('{}PARABÉNS! VOCÊ GANHOU'.format('\033[1:32m'))
    if computador == 3:
        if jogador == 1:
            print('{}PARABÉNS! VOCÊ GANHOU'.format('\033[1:32m'))
        elif jogador == 2:
            print('{}VOCÊ PERDEU!'.format('\033[1:31m'))
        elif jogador == 3:
            print('{}EMPATE'.format('\033[1:33m'))
