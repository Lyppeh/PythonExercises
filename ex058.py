from random import  randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual é?''')
palpite = int(input('Qual o seu palpite?: '))
while palpite != computador:
    palpite = int(input('Palpite errado tente novamente: '))