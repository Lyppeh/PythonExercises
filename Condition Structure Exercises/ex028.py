from random import randint
from time import sleep
computador = randint(0, 5)
print('=-=' * 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?: '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número: {} e nao no número: {}'.format(computador, jogador))