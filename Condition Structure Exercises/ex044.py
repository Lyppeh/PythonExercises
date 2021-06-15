print('='*25, 'LOJAS BLACK', '='*25)
preço = float(input('Qual o preço das compras? R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista no dinheiro
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual é a opção? '))

if escolha == 1:
    total = preço - (preço * 10 /100)
    print('Sua compra que custava R${:.2f} com 10% de desconto custará R${:.2f}'.format(preço, total))
elif escolha == 2:
    total = preço - (preço * 5/100)
    print('Sua compra que custava R${:.2f} com 5% de desconto custará R${:.2f}'.format(preço, total))
elif escolha == 3:
    total = preço / 2
    print('Sua compra de R${:.2f} dividida em 2x terá parcelas de R${:.2f}'.format(preço, total))
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas deseja dividir: '))
    juros = preço + (preço * 20/100)
    total = juros / parcelas
    print('Sua compra de R${:.2f} com 20% de juros será de R${:.2f}'.format(preço, juros))
    print('Dividida em {}x terá parcelas de {:.2f}'.format(parcelas, total))
else:
    print('{}OPÇÃO INVALIDA{}, Escolha uma opçâo valida'.format('\033[1:31m', '\033[m'))



