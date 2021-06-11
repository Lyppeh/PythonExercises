km = float(input('Quantos Kilometros rodados?:'))
d = int(input('Quantos dias alugados?:'))
pago = (km*0.15) + (d*60)
print('O total a ser pago é de R${:.2f}'.format(pago))
