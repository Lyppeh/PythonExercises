frase = str(input('Digite uma frase: ')) .strip() .upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += junto[letra]
print('O inverso da palavra {} é {}'.format(frase, inverso))
if junto == inverso:
    print('Temos um palindromo')
else:
    print('A frase não é um palindromo')


